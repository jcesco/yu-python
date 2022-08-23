class QuizBrain():
    """Models a quiz"""

    def __init__(self, question_list):
        """Initializes quiz and generates attributes, needs a question list"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Provides next question in the question list"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Returns True if there are question remaining"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Checks if user answered correctly and tracks correct answers"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
