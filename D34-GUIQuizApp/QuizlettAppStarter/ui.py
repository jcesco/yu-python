from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:            #PascalCase


    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain

        # UI Window
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Board
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Question Area
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        green_check_image = PhotoImage(file="./images/true.png")
        self.green_check = Button(image=green_check_image, highlightthickness=0, command=self.check_answer_true)
        self.green_check.grid(row=2, column=0)
        red_x_image = PhotoImage(file="./images/false.png")
        self.red_x = Button(image=red_x_image, highlightthickness=0, command=self.check_answer_false)
        self.red_x.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.green_check.config(state="disabled")
            self.red_x.config(state="disabled")


    def check_answer_true(self):
        is_correct = self.quiz.check_answer("True")
        self.provide_feedback(is_correct)

    def check_answer_false(self):
        is_correct = self.quiz.check_answer("False")
        self.provide_feedback(is_correct)

    def provide_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        #self.canvas.config(bg="white")
