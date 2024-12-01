# English Grammar Proficiency Quiz Application

## Project Description
The English Grammar Proficiency Quiz Application is a fun and interactive platform designed to help users improve their English grammar skills. The application allows users to practice grammar through quizzes, track their progress, and receive feedback for their answers. It features a user-friendly interface, performance tracking, and sound effects to create an engaging learning experience.

---

## Features
- **User Authentication**: Login and Sign-Up functionalities for personalized experiences.
- **Random Quiz Generation**: Each quiz is unique with randomly fetched questions.
- **Performance Tracking**: Tracks user scores and provides progress feedback.
- **CRUD Operations**: Add, delete, update, and view quiz questions in the database.
- **Sound Effects**: Enhances engagement with sound feedback for correct/incorrect answers.
- **Feedback Mechanism**: Displays correct answers for wrongly answered questions.
- **Admin Panel (Optional)**: Allows management of users, questions, and app settings.

---

## Screens/Windows
1. **Home Page**: Brief introduction and navigation options for users.
2. **Sign-Up Page**: For new user registration.
3. **Login Page**: Secure access for registered users.
4. **Quiz Page**: Displays random grammar questions with multiple-choice answers.
5. **Results Page**: Provides feedback on incorrect answers and overall performance.
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
    git clone https://github.com/your-repo-url/grammar-quiz.git
    cd grammar-quiz
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

## Future Enhancements
- Mobile compatibility.
- Multiplayer quiz mode.
- Progress analytics dashboard with graphs.
- Speech recognition for answering questions.
