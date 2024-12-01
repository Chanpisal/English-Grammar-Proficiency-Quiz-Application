import sqlite3

def fetch_questions():
    try:
        # Connect to the database
        conn = sqlite3.connect("english_grammar_quiz.db")
        cursor = conn.cursor()

        # Fetch all questions
        cursor.execute("SELECT * FROM Questions;")
        rows = cursor.fetchall()

        # Check if any data exists
        if rows:
            print("Fetched Questions:")
            for row in rows:
                print(row)
        else:
            print("No questions found in the Questions table.")

    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# Execute the function
if __name__ == "__main__":
    fetch_questions()
