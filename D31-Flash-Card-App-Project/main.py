from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 40, "bold")

# -------------- DATA IMPORT -------------- #
current_card = {}
words_to_learn = {}

try:
    saved_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("./data/french_words.csv")
    words_to_learn = og_data.to_dict(orient="records")
else:
    words_to_learn = saved_data.to_dict(orient="records")


# -------------- FUNCTIONS -------------- #
def generate_f_word():
    """Display new French word"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    flashcard_canvas.itemconfig(flashcard_background, image=flashcard_front_background)
    flashcard_canvas.itemconfig(flashcard_title, text="French", fill="black")
    flashcard_canvas.itemconfig(flashcard_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    """Delete French word from word bank if known by user"""
    words_to_learn.remove(current_card)
    print(f"You have {len(words_to_learn)} words remaining to learn.")
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    generate_f_word()


def flip_card():
    """Display English word"""
    flashcard_canvas.itemconfig(flashcard_background, image=flashcard_back_background)
    flashcard_canvas.itemconfig(flashcard_title, text="English", fill="white")
    flashcard_canvas.itemconfig(flashcard_word, text=current_card["English"], fill="white")


# -------------- UI SETUP -------------- #
# UI Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Flashcard
flashcard_canvas = Canvas(height=526, width=800)
flashcard_front_background = PhotoImage(file="./images/card_front.png")
flashcard_back_background = PhotoImage(file="./images/card_back.png")
flashcard_background = flashcard_canvas.create_image(400, 263, image=flashcard_front_background)
flashcard_title = flashcard_canvas.create_text(400, 150, text="", font=FONT_TITLE)
flashcard_word = flashcard_canvas.create_text(400, 263, text="", font=FONT_WORD)
flashcard_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
red_x_image = PhotoImage(file="./images/wrong.png")
red_x = Button(image=red_x_image, highlightthickness=0, command=generate_f_word)
red_x.grid(row=1, column=0)
green_check_image = PhotoImage(file="./images/right.png")
green_check = Button(image=green_check_image, highlightthickness=0, command=known_word)
green_check.grid(row=1, column=1)

generate_f_word()

window.mainloop()
