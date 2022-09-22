from tkinter import *


def button_clicked(miles):
    return miles * 1.60934


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=10)

# Entry @ (0,1)
input_field = Entry(width=10)
input_field.grid(column=1, row=0)

# Text @ (0,2)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Text @ (1,0)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# Text @ (1,1)
kilometers = 0
kilometers_label = Label(text=f"{kilometers}")
kilometers_label.grid(column=1, row=1)

# Text @ (1,2)
km_unit_label = Label(text="Km")
km_unit_label.grid(column=2, row=1)


# Button @ (2,1)
def convert():
    miles = int(input_field.get())
    kilo = miles * 1.60934
    kilometers_label.config(text=f"{kilo}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

# Keep window open
window.mainloop()
