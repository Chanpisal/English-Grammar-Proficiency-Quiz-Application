import sqlite3

def delete_duplicate_questions():
    try:
        # Connect to the database
        conn = sqlite3.connect("english_grammar_quiz.db")
        cursor = conn.cursor()

        # Find duplicate questions (based on the question_text, option_a, option_b, option_c, option_d, and correct_option)
        cursor.execute("""
        WITH DuplicateQuestions AS (
            SELECT MIN(question_id) AS keep_id
            FROM Questions
            GROUP BY question_text, option_a, option_b, option_c, option_d, correct_option
            HAVING COUNT(*) > 1
        )
        DELETE FROM Questions
        WHERE question_id NOT IN (SELECT keep_id FROM DuplicateQuestions);
        """)

        # Commit the changes
        conn.commit()

        print("Duplicate questions deleted successfully!")

    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        conn.close()

# Call the function to delete duplicates
delete_duplicate_questions()
