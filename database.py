import sqlite3
import os

# Database file path
DB_FILE = "english_grammar_quiz.db"

def get_connection():
    """
    Establish a connection to the database.
    Returns:
        sqlite3.Connection: Database connection object.
    """
    return sqlite3.connect(DB_FILE)


def setup_database():
    """
    Sets up the database by creating necessary tables and indexes.
    This method is called during application initialization.
    """
    try:
        # Connect to the database
        conn = get_connection()
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
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL CHECK (correct_option IN ('a', 'b', 'c', 'd')),
            feedback TEXT NOT NULL
        );
        """)

        # Create the Scores table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Scores (
            score_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            date_taken TEXT NOT NULL, -- ISO 8601 format: 'YYYY-MM-DD HH:MM:SS'
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

        # Create indexes to improve query performance
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
        print(f"An error occurred during database setup: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()


def fetch_random_questions(limit):
    """
    Fetch random questions from the Questions table.
    Args:
        limit (int): Number of questions to fetch.
    Returns:
        list: A list of tuples containing question data.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_option, feedback
        FROM Questions
        ORDER BY RANDOM()
        LIMIT ?;
        """, (limit,))
        questions = cursor.fetchall()
        return questions
    except sqlite3.Error as e:
        print(f"Error fetching questions: {e}")
        return []
    finally:
        if conn:
            conn.close()
