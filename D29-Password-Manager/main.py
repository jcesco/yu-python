from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    num_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + num_list
    random.shuffle(password_list)

    password_generated = "".join(password_list)

    password_field.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """Saves website, e-mail/username and password fields to a text file"""

    # Extract text from fields
    website = web_entry.get()
    email_user = username_field.get()
    pw = password_field.get()

    # Validate website and password fields have text
    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        # Verify information with user and save
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_user} "
                                                              f"\nPassword: {pw} \nIs it ok to save?")

        if is_ok:
            with open("./data.text", 'a') as datafile:
                datafile.write(f"{website} | {email_user} | {pw}\n")

                # Reset fields
                web_entry.delete(0, 'end')
                username_field.delete(0, 'end')
                username_field.insert(0, 'example@e-mail.com')
                password_field.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
# Create window for password manager
window = Tk()
window.title("Password Manager Pro")
window.config(padx=20, pady=20)

# Create image for password manager
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website text
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

# Website Entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()


# Email/UN text
username = Label(text="Email/Username:")
username.grid(column=0, row=2)

# Email/UN Entry
username_field = Entry(width=35)
username_field.grid(column=1, row=2, columnspan=2)
username_field.insert(0, "example@e-mail.com")

# Password text
password = Label(text="Password:")
password.grid(column=0, row=3)

# Password Entry
password_field = Entry(width=23)
password_field.grid(column=1, row=3)

# Password generate button
password_gen = Button(text="Generate Password", width=14, font=("Arial", 7), command=generate_password)
password_gen.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", padx=0, pady=0, width=35, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
