import sqlite3
import os
from flask import (Flask, render_template, request, redirect, url_for, flash,
                   g, session, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, UserMixin, login_user, logout_user,
                         login_required, current_user)

# Import the workout plan data
from workout_plan import WORKOUT_PLAN, PRIORITY_ADDONS, NUTRITION_GUIDE

# --- Configuration ---
DATABASE = 'database.db'
SECRET_KEY = os.urandom(24) # Generate a random secret key
# In production, set a fixed SECRET_KEY, don't regenerate it every time!
# e.g., SECRET_KEY = 'your_very_secret_and_unguessable_key_here'

app = Flask(__name__)
app.config.from_object(__name__)

# --- Database Setup ---
def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row # Return rows as dict-like objects
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

def init_db():
    """Initializes the database using schema.sql"""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print("Initialized the database.")

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()

# --- User Authentication (Flask-Login) ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Redirect here if @login_required fails
login_manager.login_message_category = "warning"

class User(UserMixin):
    """Simple User class for Flask-Login"""
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    """Loads user from DB for session management"""
    db = get_db()
    user_row = db.execute('SELECT id, username FROM user WHERE id = ?', (user_id,)).fetchone()
    if user_row:
        return User(id=user_row['id'], username=user_row['username'])
    return None

# --- Routes ---
@app.route('/')
@login_required
def index():
    """Shows the main workout plan page"""
    db = get_db()
    progress_rows = db.execute(
        'SELECT checkbox_id FROM progress WHERE user_id = ?', (current_user.id,)
    ).fetchall()
    user_progress = {row['checkbox_id'] for row in progress_rows} # Set for fast lookups

    return render_template('index.html',
                           workout_plan=WORKOUT_PLAN,
                           user_progress=user_progress,
                           priority_addons=PRIORITY_ADDONS,
                           nutrition_guide=NUTRITION_GUIDE)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles user login and registration"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        action = request.form['action'] # 'login' or 'register'
        db = get_db()
        error = None
        user_row = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()

        if action == 'login':
            if user_row is None or not check_password_hash(user_row['password'], password):
                error = 'Incorrect username or password.'
            else:
                user_obj = User(id=user_row['id'], username=user_row['username'])
                login_user(user_obj)
                flash('Login successful!', 'success')
                return redirect(url_for('index'))

        elif action == 'register':
            if user_row is not None:
                error = f'Username "{username}" is already taken.'
            else:
                # Register new user
                db.execute('INSERT INTO user (username, password) VALUES (?,?)',
                           (username, generate_password_hash(password)))
                db.commit()
                # Log in the new user immediately
                new_user_row = db.execute('SELECT * FROM user WHERE username = ?', (username,)).fetchone()
                user_obj = User(id=new_user_row['id'], username=new_user_row['username'])
                login_user(user_obj)
                flash('Registration successful! You are now logged in.', 'success')
                return redirect(url_for('index'))

        if error:
            flash(error, 'danger')

    # Pass a dummy form object if needed by template, else remove
    # from form tag in login.html
    class DummyForm: csrf_token = None
    return render_template('login.html', form=DummyForm())


@app.route('/logout')
@login_required
def logout():
    """Logs the user out"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/update_progress', methods=['POST'])
@login_required
def update_progress():
    """Endpoint to save checkbox state (called via JavaScript)"""
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
            # Add or ignore if already exists (UNIQUE constraint handles this)
            db.execute('INSERT OR IGNORE INTO progress (user_id, checkbox_id) VALUES (?, ?)',
                       (current_user.id, checkbox_id))
        else:
            # Remove if it exists
            db.execute('DELETE FROM progress WHERE user_id = ? AND checkbox_id = ?',
                       (current_user.id, checkbox_id))
        db.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        db.rollback() # Rollback changes on error
        print(f"Database error: {e}") # Log error server-side
        return jsonify({"status": "error", "message": "Database error"}), 500


if __name__ == '__main__':
    # Check if the database exists, if not, initialize it
    # This is okay for development, but for deployment, run 'flask initdb' manually once.
    if not os.path.exists(app.config['DATABASE']):
        with app.app_context(): # Need app context to access g and app.open_resource
             init_db()
    app.run(debug=True) # debug=True is helpful for development, turn off for production 
