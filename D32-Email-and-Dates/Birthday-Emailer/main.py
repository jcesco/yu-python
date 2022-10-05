import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "GeeTester696@gmail.com"
MY_PASSWORD = "wdbijimadlgmkehp"
LETTERS = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

# Get data from csv
bday_data = pd.read_csv("./birthdays.csv")

# Generate new dictionary from pandas dataframe using dictionary comprehension
bday_dict = {(row.month, row.day): [row.nombre, row.email, row.year, row.month, row.day]
             for(index, row) in bday_data.iterrows()}

# Get today's date
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# Look if there is a bday today
if (today_month, today_day) in bday_dict:

    # Choose random letter
    with open(random.choice(LETTERS)) as letter:
        template_letter = letter.read()

    # Create custom letter
    placeholder = "[NAME]"
    bday_person = bday_dict[today_month, today_day][0]
    custom_letter = template_letter.replace(placeholder, bday_person)

    # Send custom letter
    bday_email = bday_dict[today_month, today_day][1]
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=bday_email,
                            msg=f"Subject: Another trip around the sun!\n\n{custom_letter}")
