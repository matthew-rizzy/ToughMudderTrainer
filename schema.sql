-- schema.sql
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS progress;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  custom_weights TEXT DEFAULT '{}' -- Add this line (stores JSON string)
);

CREATE TABLE progress (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  checkbox_id TEXT NOT NULL, -- e.g., "week1-wed-task0", "week1-thu-task1"
  FOREIGN KEY (user_id) REFERENCES user (id),
  UNIQUE (user_id, checkbox_id) -- Each user can only check a specific box once
);
