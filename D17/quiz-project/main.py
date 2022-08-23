from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Generate blank list for question bank
question_bank = []

# Append question bank with data from data file
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

# Instantiate quiz brain and display first question
quiz = QuizBrain(question_bank)
quiz.next_question()

# Cycle through all question until all questions have been shown
while quiz.still_has_questions():
    quiz.next_question()

# Tell user quiz is finished and display final score
print("You completed the quiz!")
print(f"Your final score was {quiz.score}/{len(question_bank)}")