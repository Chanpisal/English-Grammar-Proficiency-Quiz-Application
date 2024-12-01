import sqlite3
import datetime

try:
    # Connect to the database
    conn = sqlite3.connect("english_grammar_quiz.db")
    cursor = conn.cursor()

    # Create the Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """)

    # Create the Questions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Questions (
        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,       -- Renamed for consistency
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL CHECK (correct_option IN ('a', 'b', 'c', 'd')), -- Validate correct options
        feedback TEXT NOT NULL
    );
    """)

    # Create the Scores table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Scores (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        date_taken TEXT NOT NULL,          -- Use ISO 8601 format: 'YYYY-MM-DD HH:MM:SS'
        level_assessed TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    """)

    # Create the Settings table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Settings (
        user_id INTEGER PRIMARY KEY,
        background_music INTEGER DEFAULT 1,
        sound_effects INTEGER DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    """)

    # Add indexes to improve performance on frequently queried columns
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_user_id_scores ON Scores(user_id);
    """)
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_user_id_settings ON Settings(user_id);
    """)

    # Commit changes
    conn.commit()
    print("Database and tables created successfully!")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    if conn:
        conn.close()
