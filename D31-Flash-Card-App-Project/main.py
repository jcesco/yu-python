from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"


# -------------- UI SETUP -------------- #
# UI Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

# Flashcard
flashcard_canvas = Canvas(height=526, width=800)
flashcard_front_background = PhotoImage(file="./images/card_front.png")
flashcard_back_background = PhotoImage(file="./images/card_back.png")
flashcard_canvas.create_image(400, 263, image=flashcard_front_background)
flashcard_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
red_x_image = PhotoImage(file="./images/wrong.png")
red_x = Button(image=red_x_image, highlightthickness=0)
red_x.grid(row=1, column=0)
green_check_image = PhotoImage(file="./images/right.png")
green_check = Button(image=green_check_image, highlightthickness=0)
green_check.grid(row=1, column=1)

window.mainloop()
