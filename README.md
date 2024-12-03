# English Grammar Proficiency Quiz Application

## Project Description
The English Grammar Proficiency Quiz Application is a fun and interactive platform designed to help users improve their English grammar skills. The application allows users to practice grammar through quizzes, track their progress, and receive feedback for their answers as well as the link to access the website for further improvement. It features a user-friendly interface, performance tracking, and sound effects to create an engaging learning experience.

---

## Features
- **User Authentication**: Login and Sign-Up functionalities for personalized experiences.
- **Random Quiz Generation**: Each quiz is unique with randomly fetched questions.
- **Performance Tracking**: Tracks user scores and provides progress feedback.
- **CRUD Operations**: Add, delete, update, and view quiz questions in the database.
- **Sound Effects**: Enhances engagement with sound feedback for correct/incorrect answers.
- **Feedback Mechanism**: Displays correct answers for wrongly answered questions and the link to access the website for further improvement .
- **Admin Panel (Optional)**: Allows management of users, questions, and app settings.

---

## Screens/Windows
1. **Home Page**: Brief introduction and navigation options for users.
2. **Sign-Up Page**: For new user registration.
3. **Login Page**: Secure access for registered users.
4. **Quiz Page**: Displays random grammar questions with multiple-choice answers.
5. **Results Page**: Provides feedback on incorrect answers, overall performance, and the link to access the website.
6. **Settings Page (Optional)**: Adjust sound and difficulty settings.
7. **Admin Dashboard (Optional)**: Manage content and user settings.

---

## Database Design
### Tables
- **Users**: Stores user credentials (username, password).
- **Questions**: Stores grammar questions, options, and correct answers.
- **Scores**: Tracks user performance (user ID, score, date).
- **Settings**: Stores user preferences (e.g., sound effects).

### Database File
- **File Name**: `english_grammar_quiz.db`.

---

## Dependencies
- **Python Version**: 3.8 or higher.
- **SQLite**: Comes pre-installed with Python.
- **Python Libraries**:
  - `sqlite3`: For database operations.
  - `pygame`: For sound effects. Install it with:
    ```bash
    pip install pygame
    ```

---

## Installation Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Chanpisal/English-Grammar-Proficiency-Quiz-Application.git
    cd Final_project
    ```
2. **Set Up the Database**:
    - Run the following scripts to initialize the database and add sample data:
        ```bash
        python create_database.py
        python insert_question.py
        ```
3. **Run the Application**:
    - Start the application by executing the main script:
        ```bash
        python main.py
        ```

4. **Configuration Settings**:
    - Ensure the database file (`english_grammar_quiz.db`) is in the project directory.
    - Adjust settings like the number of quiz questions or sound preferences in `main.py` or via the app's settings page.

---

## Usage Instructions
1. **Sign-Up/Login**: Create an account or log in to start the quiz.
2. **Quiz**: Answer random grammar questions and receive instant feedback.
3. **Results**: View detailed results and explanations for incorrect answers.
4. **Admin (Optional)**: Manage quiz content and settings.

---

## Challenges and Solutions
- **Random Question Selection**: Used `ORDER BY RANDOM()` in SQL queries to ensure randomization.
- **Error Handling**: Implemented to prevent app crashes and guide users when errors occur.
- **Feedback**: Displays correct answers dynamically after quiz completion for better learning.

---

## Sound Files

The application includes various sound files to enhance user interaction. These files are used for:

- **Feedback**: Sounds for correct and incorrect answers as well as congraduation.
- **Background Music**: Optional background audio for the quiz.

### File Format and Location

- **File Format**: `.mp3` (ensure all sound files are in the `sounds/` directory).

### Usage

Place sound files in the `sounds/` directory in the project root. The application will load these files automatically for sound effects during quizzes.

---

## Directory Structure

EnglishGrammarQuiz/
├── backend/
│   ├── main.py                # Entry point of the application
│   ├── database.py            # Handles database connections and queries
│   ├── create_database.py     # Creates the necessary database structure
│   ├── insert_question.py     # Inserts quiz questions into the database
│   ├── verify_data.py         # Verifies if the database is properly populated
│   ├── delete.py              # Deletes user data or resets the database
│   ├── quiz_logic.py          # Contains the logic for the quiz functionality
│   ├── sound.py               # Plays sound effects using Pygame
├── frontend/
│   ├── gui.py                 # Manages the graphical user interface using Tkinter
├── database/
│   ├── english_grammar_quiz.db # SQLite database file
│   ├── quiz_db.sql            # SQL structure for the quiz database (if applicable)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and instructions

---

## Future Enhancements
- Mobile compatibility.
- Multiplayer quiz mode.
- Progress analytics dashboard with graphs.
- Speech recognition for answering questions.

---

## References
1. **Online Tutorials**:
- Akashgiricse. (n.d.). GitHub - akashgiricse/lets-quiz: A quiz website for organizing online quizzes and tests. It’s build using Python/Django and Bootstrap4 frameworks. GitHub. https://github.com/akashgiricse/lets-quiz.git
- Bro Code. (2022, November 23). Create a QUIZ GAME with Python [Video]. YouTube. https://www.youtube.com/watch?v=zehwgTB0vV8
- GeeksforGeeks. (2023, February 23). Python Quiz Application Project. GeeksforGeeks. https://www.geeksforgeeks.org/python-quiz-application-project/
- Lodha, S. (2024, September 22). Quiz Application Using Python With Source Code - CodeWithCurious. CodeWithCurious. https://codewithcurious.com/projects/quiz-application-using-python/
- Trinity software academy. (2020, September 30). How to build a Quiz app with Python Tkinter [Video]. YouTube. https://www.youtube.com/watch?v=5smq0hCANaE
1. **Collaboration**:
- Discussed key challenges and ideas with peers and professors for feedback and improvement.
