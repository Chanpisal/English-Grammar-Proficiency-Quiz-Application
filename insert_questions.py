import sqlite3

# Connect to the database
conn = sqlite3.connect("english_grammar_quiz.db")
cursor = conn.cursor()

# List of questions with corrected field names
questions_data = [
    ("I can’t remember where I ___ my keys.", "put", "puts", "putting", "was putting", "a", "Past simple 'put' is used for completed actions."),
    ("He said he ___ finish the project on time.", "will", "can", "would", "could", "c", "'Would' is used for reported speech in the past."),
    ("If I had more time, I ___ learn another language.", "will", "would", "could", "should", "b", "'Would' is used in second conditional sentences for hypothetical situations."),
    ("We haven’t seen her ___ last week.", "for", "since", "in", "by", "b", "'Since' is used to indicate the starting point of an action or event."),
    ("The cake ___ by the time I arrived.", "ate", "was eating", "had been eaten", "is eaten", "c", "Past perfect passive ('had been eaten') is used to describe actions completed before another event."),
    ("They managed to finish the work ___ they had little time.", "despite", "although", "however", "even", "b", "'Although' is a conjunction used to contrast two ideas."),
    ("You’d better ___ your umbrella. It looks like rain.", "take", "taking", "to take", "took", "a", "'Take' is the correct form after 'you'd better' for advice."),
    ("We were surprised ___ the news.", "to hear", "by hearing", "with hearing", "heard", "a", "'To hear' is the correct form with 'surprised.'"),
    ("If he ___ the truth, he wouldn’t have been so surprised.", "had known", "knows", "would know", "will know", "a", "Past perfect 'had known' is used in third conditional sentences."),
    ("I was wondering if you ___ me a favor.", "can do", "could do", "would do", "will do", "b", "'Could' is polite when making a request."),
    ("It’s high time we ___ a decision about the proposal.", "make", "made", "are making", "have made", "b", "'Made' is used after 'It's high time' to express urgency with a past simple verb."),
    ("No sooner ___ than it started raining.", "had we left", "we had left", "we left", "have we left", "a", "Inversions with 'No sooner' use past perfect and auxiliary verbs."),
    ("I object to ___ treated unfairly.", "being", "be", "have been", "having", "a", "'Being' is the correct form after 'object to.'"),
    ("Only after we discussed it ___ to understand the problem.", "we started", "we start", "did we start", "have we started", "c", "Inversions require auxiliary verbs in questions and emphatic sentences."),
    ("The manager insisted that the report ___ before Friday.", "is completed", "completed", "be completed", "was completed", "c", "Subjunctive form 'be completed' is used in formal requests or requirements."),
    ("Had I known about the delay, I ___ waited.", "wouldn’t have", "won’t have", "couldn’t have", "hadn’t", "a", "'Wouldn’t have' expresses regret about a past action."),
    ("Scarcely ___ the meeting started when the fire alarm went off.", "had", "has", "have", "will", "a", "Inversions with 'Scarcely' require past perfect."),
    ("The research findings, ___, caused quite a debate.", "which were unexpected", "that were unexpected", "who were unexpected", "what were unexpected", "a", "'Which' introduces non-defining relative clauses."),
    ("Were it not for his help, we ___.", "will fail", "would fail", "would have failed", "failed", "c", "'Would have failed' is used in conditional statements about the past."),
    ("She ___ go to the party if she finishes her homework.", "will", "would", "can", "could", "b", "'Would' is used in conditional sentences to talk about possible future events."),
    ("I ___ never seen such a beautiful sunset before.", "have", "had", "am", "was", "a", "Present perfect ('have seen') is used to describe experiences up to the present."),
    ("By the time he arrives, we ___ already left.", "have", "had", "will", "would", "b", "Past perfect ('had left') is used to indicate an action completed before another past event."),
    ("She ___ take the bus because her car is broken.", "has to", "had to", "will", "would", "a", "'Has to' is used to express necessity in the present."),
    ("If I ___ enough money, I would have bought a new phone.", "have", "had", "will have", "would have", "b", "Past perfect ('had') is used in the third conditional to express a hypothetical past situation."),
    ("He didn't know whether he ___ go to the meeting or not.", "will", "would", "can", "could", "b", "'Would' is used for reported speech in indirect questions."),
    ("I can't believe he ___ finished the project already.", "has", "had", "is", "was", "a", "Present perfect ('has finished') is used for actions that have an impact on the present."),
    ("They ___ always make excuses when they are late.", "are", "were", "will", "have", "a", "Present continuous ('are making') describes actions happening now or in the near future."),
    ("If I were you, I ___ apologize to her immediately.", "will", "would", "could", "might", "b", "Second conditional uses 'would' to talk about hypothetical situations."),
    ("She ___ hard every day to improve her skills.", "works", "work", "is working", "has worked", "a", "Simple present ('works') is used for habits or routines."),
    ("It was the first time I ___ a train before." , "took", "have taken", "take", "had taken", "d", "Past perfect ('had taken') is used to describe an event completed before another event."),
    ("They asked me if I ___ to the party with them.", "would come", "come", "will come", "could come", "a", "Indirect speech uses 'would' for reported questions."),
    ("By the end of this year, they ___ finished the project.", "will have", "will", "have", "had", "a", "Future perfect ('will have finished') is used to describe an action that will be completed before a certain time in the future."),
    ("I haven't seen him ___ last summer.", "since", "for", "in", "by", "a", "'Since' is used to indicate the starting point of an action or event."),
    ("The movie ___ by the time we arrived at the theater.", "had started", "started", "was starting", "had been started", "a", "Past perfect ('had started') is used to describe an event completed before another past action."),
    ("I don't know if I ___ attend the meeting tomorrow.", "can", "will", "could", "should", "a", "Present simple ('can') is used for ability or possibility."),
    ("By the time you read this, I ___ gone to the store.", "will have", "have", "had", "will", "a", "Future perfect ('will have gone') is used to describe an action that will be completed before a specific future time."),
    ("She was so tired that she ___ go to bed early.", "has to", "had to", "is to", "was to", "b", "Past simple ('had to') is used for necessity or obligation in the past."),
    ("He is the kind of person who ___ help others without expecting anything in return.", "can", "could", "will", "would", "c", "Simple present ('will') is used for general truths or facts."),
    ("We were unable to find a solution because we ___ had enough time.", "didn't", "haven't", "hadn't", "don't", "c", "Past perfect ('hadn't') is used to show something was incomplete before another past event."),
    ("I can’t find my phone. I think I ___ it at the café.", "left", "leave", "have left", "had left", "a", "Simple past ('left') is used for actions completed at a specific time in the past."),
    ("If you ___ me, I would have helped you.", "ask", "asked", "had asked", "will ask", "b", "Past perfect ('had asked') is used in third conditional to express a hypothetical past situation."),
]

# Insert questions while checking for duplicates
try:
    # Check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Questions';")
    if not cursor.fetchone():
        raise Exception("The 'Questions' table does not exist. Please create the table first.")
    
    # Retrieve existing questions to avoid duplicates
    cursor.execute("SELECT question_text FROM Questions;")
    existing_questions = set(row[0] for row in cursor.fetchall())

    # Filter out questions that are already in the database
    questions_data = [q for q in questions_data if q[0] not in existing_questions]

    # Insert the non-duplicate questions
    cursor.executemany("""
    INSERT INTO Questions (question_text, option_a, option_b, option_c, option_d, correct_option, feedback)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, questions_data)

    conn.commit()
    print(f"{len(questions_data)} questions inserted successfully!")

except sqlite3.Error as e:
    print(f"Database error occurred: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection
    conn.close()
