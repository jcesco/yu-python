from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# data.txt
# webste | email | pw
#delete function, insert method for tikinter

def save_data():

    with open("./data.text", 'a') as datafile:
        datafile.write(f"{web_entry.get()} | {username_field.get()} | {password_field.get()}\n")

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
password_gen = Button(text="Generate Password", width=14, font=("Arial", 7) )
password_gen.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", padx=0, pady=0, width=35, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()