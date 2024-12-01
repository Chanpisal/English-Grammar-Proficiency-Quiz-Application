from collections import namedtuple

# Define a namedtuple for levels
Level = namedtuple('Level', ['code', 'description'])

# Map levels to score ranges
LEVELS = [
    (3, Level("A1", "Beginner Level")),
    (5, Level("B1", "Intermediate Level")),
    (7, Level("B2", "Upper-Intermediate Level")),
    (10, Level("C1", "Advanced Level"))
]

# Map feedback to score ranges
FEEDBACK = [
    (4, "Keep practicing to improve your grammar skills!"),
    (7, "Good job! You're getting there."),
    (10, "Excellent work! You have a strong grasp of grammar.")
]

def get_feedback_by_score(score):
    """Return feedback based on the score."""
    for max_score, feedback in FEEDBACK:
        if score <= max_score:
            return feedback
    return "Invalid score."

def get_level_by_score(score):
    """Return level and description based on the score."""
    for max_score, level in LEVELS:
        if score <= max_score:
            return level
    return Level("N/A", "Invalid score.")

# Example Usage
if __name__ == "__main__":
    score = 8
    feedback = get_feedback_by_score(score)
    level = get_level_by_score(score)
    print(f"Score: {score}")
    print(f"Feedback: {feedback}")
    print(f"Level: {level.code} - {level.description}")