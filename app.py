import sqlite3
import os
import json # <-- Add json import
from flask import (Flask, render_template, request, redirect, url_for, flash,
                   g, session, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, UserMixin, login_user, logout_user,
                         login_required, current_user)

# Import the workout plan data
from workout_plan import WORKOUT_PLAN, PRIORITY_ADDONS, NUTRITION_GUIDE

# --- Configuration ---
DATABASE = 'database.db'
SECRET_KEY = os.urandom(24)
# SECRET_KEY = 'your_very_secret_and_unguessable_key_here' # Use a fixed key in production

app = Flask(__name__)
app.config.from_object(__name__)

# --- Database Setup ---
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print("Initialized the database.")

@app.cli.command('initdb')
def initdb_command():
    init_db()

# --- User Authentication (Flask-Login) ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "warning"

class User(UserMixin):
    """User class now holds custom weights"""
    def __init__(self, id, username, custom_weights_json='{}'):
        self.id = id
        self.username = username
        try:
            # Parse JSON string into dict when User object is created
            self.custom_weights = json.loads(custom_weights_json or '{}')
        except json.JSONDecodeError:
            print(f"Warning: Could not parse custom_weights JSON for user {id}")
            self.custom_weights = {} # Default to empty dict on error

@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    # Fetch custom_weights along with id and username
    user_row = db.execute('SELECT id, username, custom_weights FROM user WHERE id = ?', (user_id,)).fetchone()
    if user_row:
        # Pass the JSON string to the User constructor
        return User(id=user_row['id'], username=user_row['username'], custom_weights_json=user_row['custom_weights'])
    return None

# --- Routes ---
@app.route('/')
@login_required
def index():
    db = get_db()
    progress_rows = db.execute(
        'SELECT checkbox_id FROM progress WHERE user_id = ?', (current_user.id,)
    ).fetchall()
    user_progress = {row['checkbox_id'] for row in progress_rows}

    # Pass the parsed custom_weights dict from the current_user object
    return render_template('index.html',
                           workout_plan=WORKOUT_PLAN,
                           user_progress=user_progress,
                           user_custom_weights=current_user.custom_weights, # Pass parsed dict
                           priority_addons=PRIORITY_ADDONS,
                           nutrition_guide=NUTRITION_GUIDE)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # ... (login/register logic remains the same - it doesn't need custom_weights initially)
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form.get('action')
        db = get_db()
        error = None
        user_row = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()

        if action == 'login':
            if user_row is None or not check_password_hash(user_row['password'], password):
                error = 'Incorrect username or password.'
            else:
                # Pass the loaded JSON string during login
                user_obj = User(id=user_row['id'], username=user_row['username'], custom_weights_json=user_row['custom_weights'])
                login_user(user_obj)
                flas('Login successful!', 'success')
                # Fetch redirect URL safely
                next_page = request.args.get('next')
                return redirect(next_page or url_for('index'))

        elif action == 'register':
            if user_row is not None:
                error = f'Username "{username}" is already taken.'
            else:
                # Register new user (custom_weights defaults to '{}' in DB)
                db.execute('INSERT INTO user (username, password) VALUES (?, ?)',
                           (username, generate_password_hash(password)))
                db.commit()
                # Log in the new user immediately
                new_user_row = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()
                # New user starts with empty custom weights
                user_obj = User(id=new_user_row['id'], username=new_user_row['username']) # Default '{}' will be handled
                login_user(user_obj)
                flash('Registration successful! You are now logged in.', 'success')
                return redirect(url_for('index'))

        if error:
            flash(error, 'danger')

    # Pass a dummy form object if needed by template, else remove
    class DummyForm: csrf_token = None
    return render_template('login.html', form=DummyForm())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/update_progress', methods=['POST'])
@login_required
def update_progress():
    # ... (This route remains unchanged)
    if not request.is_json:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json()
    checkbox_id = data.get('checkbox_id')
    is_checked = data.get('checked')

    if checkbox_id is None or is_checked is None:
        return jsonify({"status": "error", "message": "Missing data"}), 400

    db = get_db()
    try:
        if is_checked:
            db.execute('INSERT OR IGNORE INTO progress (user_id, checkbox_id) VALUES (?, ?)',
                       (current_user.id, checkbox_id))
        else:
            db.execute('DELETE FROM progress WHERE user_id = ? AND checkbox_id = ?',
                       (current_user.id, checkbox_id))
        db.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        db.rollback()
        print(f"Database error in update_progress: {e}")
        return jsonify({"status": "error", "message": "Database error"}), 500

# --- NEW ROUTE for updating weights ---
@app.route('/update_weight', methods=['POST'])
@login_required
def update_weight():
    if not request.is_json:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json()
    exercise_key = data.get('exercise_key') # e.g., "week1-thu-frontsquat"
    new_weight_str = data.get('weight')

    if not exercise_key or new_weight_str is None: # Check for empty string too
        return jsonify({"status": "error", "message": "Missing exercise_key or weight"}), 400

    try:
        # Attempt to convert weight to float, allow empty string to clear weight? Or require number?
        # Let's require a number or allow clearing by sending maybe 0 or empty?
        # For now, assume it's a valid number string or empty for clearing/defaulting.
        if new_weight_str == "":
             new_weight = None # Represent clearing the custom weight
        else:
            new_weight = float(new_weight_str) # Validate it's a number
            if new_weight < 0: # Basic validation
                 return jsonify({"status": "error", "message": "Weight cannot be negative"}), 400
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid weight format"}), 400

    db = get_db()
    try:
        # 1. Get current custom_weights JSON string for the user
        user_row = db.execute('SELECT custom_weights FROM user WHERE id = ?', (current_user.id,)).fetchone()
        if user_row is None: # Should not happen if user is logged in
             return jsonify({"status": "error", "message": "User not found"}), 404

        # 2. Parse JSON string to Python dict
        try:
            custom_weights_dict = json.loads(user_row['custom_weights'] or '{}')
        except json.JSONDecodeError:
             custom_weights_dict = {} # Start fresh if JSON is corrupted

        # 3. Update the dictionary
        if new_weight is None:
            # If weight is cleared, remove the key from custom weights to revert to default
            custom_weights_dict.pop(exercise_key, None)
        else:
            custom_weights_dict[exercise_key] = new_weight

        # 4. Convert back to JSON string
        updated_weights_json = json.dumps(custom_weights_dict)

        # 5. Update the database
        db.execute('UPDATE user SET custom_weights = ? WHERE id = ?', (updated_weights_json, current_user.id))
        db.commit()

        # 6. Update the current_user object in memory for consistency in the current request/session
        current_user.custom_weights = custom_weights_dict

        return jsonify({"status": "success", "message": "Weight updated"})

    except Exception as e:
        db.rollback()
        print(f"Database error in update_weight: {e}")
        return jsonify({"status": "error", "message": "Database error updating weight"}), 500

if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        with app.app_context():
             init_db()
    # Set host='0.0.0.0' to run on network, remove debug=True for production
    app.run(debug=True, host='0.0.0.0')
