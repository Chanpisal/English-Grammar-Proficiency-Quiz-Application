import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pygame
from database import setup_database, fetch_random_questions, get_connection
from sound import toggle_music, play_sound, correct_sound, incorrect_sound, congratulations_sound, background_music
from quiz_logic import get_feedback_by_score, get_level_by_score
from gui import create_label, create_button, create_entry, create_frame, clear_window
import webbrowser

# Initialize the database
setup_database()


class GrammarQuizApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Grammar Proficiency Quiz")
        self.root.geometry("800x500")  # Larger size for better layout
        self.root.configure(bg="#6a0dad")  # Purple background

        self.user_id = None
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.is_muted = False  # Mute/unmute toggle

        # Play background music
        if background_music:
            pygame.mixer.music.load(background_music)
            pygame.mixer.music.play(-1)

        self.load_login_screen()

    def load_login_screen(self):
        """Load the login screen."""
        clear_window(self.root)
        
        # Create a frame for better alignment
        login_frame = create_frame(self.root)
        login_frame.pack(pady=50)
        
        create_label(login_frame, text="Login or Sign Up", font_size=18).pack(pady=20)

        # Username Entry
        create_label(login_frame, text="Username:", font_size=14).pack(pady=5)
        username_entry = create_entry(login_frame)
        username_entry.pack(pady=5)

        # Password Entry
        create_label(login_frame, text="Password:", font_size=14).pack(pady=5)
        password_entry = create_entry(login_frame, show="*")
        password_entry.pack(pady=10)

        # Buttons with tooltips
        create_button(login_frame, text="Login",
                      command=lambda: self.login_user(username_entry.get(), password_entry.get()),
                      tooltip="Enter your credentials to log in").pack(pady=5)
        create_button(login_frame, text="Sign Up",
                      command=lambda: self.sign_up_user(username_entry.get(), password_entry.get()),
                      tooltip="Create a new account").pack(pady=5)

    def login_user(self, username, password):
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT user_id FROM Users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()
            if user:
                self.user_id = user[0]
                self.load_home_screen()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            print(f"Login error: {e}")
            messagebox.showerror("Error", "An error occurred during login.")
        finally:
            conn.close()

    def sign_up_user(self, username, password):
        """Register a new user."""
        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Account created! Please log in.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        except Exception as e:
            print(f"Sign-up error: {e}")
            messagebox.showerror("Error", "An error occurred during sign-up.")
        finally:
            conn.close()

    def load_home_screen(self):
        """Load the home screen."""
        clear_window(self.root)
        
        # Navigation frame for buttons
        nav_frame = create_frame(self.root)
        nav_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        create_button(nav_frame, text="Mute" if not self.is_muted else "Unmute",
                      command=self.toggle_music, font_size=12, width=10).pack(side=tk.LEFT, padx=5)
        create_button(nav_frame, text="Exit", command=self.root.quit, font_size=12, width=10).pack(side=tk.RIGHT, padx=5)

        # Main Screen Label
        create_label(self.root, text="Welcome to Grammar Proficiency Quiz", font_size=20).pack(pady=30)

        # Main Buttons
        main_frame = create_frame(self.root)
        main_frame.pack(pady=20)

        create_button(main_frame, text="Start the Quiz", command=self.start_quiz).pack(pady=10)
        create_button(main_frame, text="View Past Scores", command=self.view_past_scores).pack(pady=10)

    def view_past_scores(self):
        """Display past scores for the logged-in user."""
        if not self.user_id:
            messagebox.showerror("Error", "Please log in first.")
            return

        clear_window(self.root)
        create_label(self.root, text="Your Past Quiz Scores", font_size=18).pack(pady=20)

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT score, date_taken, level_assessed FROM Scores WHERE user_id = ?", (self.user_id,))
            scores = cursor.fetchall()
            conn.close()

            if scores:
                for score, date_taken, level_assessed in scores:
                    create_label(self.root, text=f"Score: {score}, Date: {date_taken}, Level: {level_assessed}",
                                 font_size=14).pack(pady=5)
            else:
                create_label(self.root, text="No past scores found.", font_size=14).pack(pady=5)

        except Exception as e:
            print(f"Error fetching scores: {e}")
            messagebox.showerror("Error", "An error occurred while fetching your past scores.")

        create_button(self.root, text="Main Menu", command=self.load_home_screen).pack(pady=20)

    def start_quiz(self):
        """Start the quiz."""
        self.questions = self.fetch_random_questions(10)
        if not self.questions:
            messagebox.showerror("Error", "No questions found in the database.")
            return
        self.current_question_index = 0
        self.score = 0
        self.start_time = datetime.now()
        self.show_question()

    def fetch_random_questions(self, limit):
        """Fetch random questions from the database."""
        return fetch_random_questions(limit)

    def show_question(self):
        """Display the current question and options."""
        clear_window(self.root)

        # Navigation Buttons
        create_button(self.root, text="Mute" if not self.is_muted else "Unmute",
                      command=self.toggle_music, font_size=10, width=10).place(x=10, y=10)
        create_button(self.root, text="Main Menu", command=self.load_home_screen, font_size=10, width=12).place(
            x=680, y=10)

        # Question Display
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            create_label(self.root, text=f"Question {self.current_question_index + 1}:", font_size=16).pack(pady=20)
            create_label(self.root, text=question[1], font_size=14, bg_color="#8a2be2").pack(pady=10)

            feedback_label = create_label(self.root, text="", font_size=12)
            feedback_label.pack(pady=10)

            for option, text in zip(['a', 'b', 'c', 'd'], question[2:6]):
                create_button(self.root, text=f"{option}) {text}",
                              command=lambda opt=option: self.check_answer(opt, question[6], question[7],
                                                                           feedback_label)).pack(pady=5)
        else:
            self.show_results()

    def check_answer(self, user_answer, correct_answer, feedback, feedback_label):
        """Check user's answer."""
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'].startswith(('a)', 'b)', 'c)', 'd)')):
                widget.config(state=tk.DISABLED)

        if user_answer == correct_answer:
            play_sound(correct_sound if not self.is_muted else None)
            self.score += 1
            feedback_label.config(text="Correct!", fg="green")
            self.root.after(1000, self.next_question)
        else:
            play_sound(incorrect_sound if not self.is_muted else None)
            feedback_label.config(text=f"Incorrect! {feedback}", fg="red")
            create_button(self.root, text="Next", command=self.next_question).pack(pady=10)

    def next_question(self):
        """Proceed to the next question."""
        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        """Display the final score, feedback, and level assessed."""
        clear_window(self.root)  # Clear the GUI window
        end_time = datetime.now()  # Calculate the end time
        time_taken = end_time - self.start_time  # Calculate total time taken
        time_taken_str = str(time_taken).split(".")[0]  # Format time taken

        # Mute/Unmute button
        create_button(self.root, text="Mute" if not self.is_muted else "Unmute",
                    command=self.toggle_music, font_size=10, width=10).place(x=10, y=10)

        # Determine the level and feedback
        level = get_level_by_score(self.score)
        feedback = get_feedback_by_score(self.score)

        # Play congratulations sound if not muted
        play_sound(congratulations_sound if not self.is_muted else None)

        # Display Results
        create_label(self.root, text="Quiz Complete!", font_size=20).pack(pady=20)
        create_label(self.root, text=f"Your Score: {self.score}/10", font_size=18).pack()
        create_label(self.root, text=f"Level Assessed: {level.code} - {level.description}", font_size=16).pack()
        create_label(self.root, text=f"Time Taken: {time_taken_str}", font_size=16).pack()
        create_label(self.root, text=feedback, font_size=14).pack(pady=10)

        # If score is below 7, suggest further improvement
        if self.score < 7:
            create_label(self.root, text="Your score indicates that further improvement in grammar may be beneficial.",
                        font_size=14, bg_color="#ffcccc").pack(pady=20)

            # Adjusting button size for better fit
            create_button(self.root, text="Click here to improve your grammar!", 
                        command=self.open_grammar_website, font_size=12, width=30).pack(pady=10)

        create_button(self.root, text="Main Menu", command=self.load_home_screen, font_size=10, width=12).place(
            x=680, y=10)

        # Save the score in the database
        self.save_score(level.code)

    def open_grammar_website(self):
        """Open a website for grammar improvement."""
        url = "https://learnenglish.britishcouncil.org/english-levels/improve-your-english-level/how-improve-your-english-grammar"  
        webbrowser.open(url)

    def save_score(self, level_assessed):
        """Save the score to the database."""
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Scores (user_id, score, date_taken, level_assessed) VALUES (?, ?, ?, ?)",
                (self.user_id, self.score, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), level_assessed)
            )
            conn.commit()
        except Exception as e:
            print(f"Error saving score: {e}")
        finally:
            conn.close()

    def toggle_music(self):
        """Mute/unmute background music."""
        self.is_muted = not self.is_muted
        toggle_music(self.is_muted)


if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarQuizApp(root)
    root.mainloop()
