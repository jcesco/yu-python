# import smtplib
#
# my_email = "GeeTester696@gmail.com"
# password = "wdbijimadlgmkehp"
#
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     #connection.starttls()  # Do Not Include This Line, breaks smtplib.SMTP_SSL
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="VeeTester696@gmail.com",
#                         msg="Subject:RingRing\n\nWaazzaap?!")
#
# # REFERENCES
# # 1. Need 2FA to make App passwords in order for smtplib to work with gmail
# # https://support.google.com/accounts/answer/185833?hl=en
# # https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year #type "now." and see other time types available
# print(now)
# print(type(now))
# print(year)
# print(type(year))
#
# day_of_week = now.weekday()
# print(day_of_week) # FYI, 0 = Monday, 1 = Tuesday
#
# date_of_birth = dt.datetime(year=1995, month=10, day=31, hour=6)
# print(date_of_birth)


import smtplib
import datetime as dt
import random

MY_EMAIL = "GeeTester696@gmail.com"
MY_PASSWORD = "wdbijimadlgmkehp"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt", 'r') as datafile:
        quotes = datafile.readlines()
        rand_quote = random.choice(quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="VeeTester696@gmail.com",
                            msg=f"Subject:Good Day\n\n{rand_quote}")