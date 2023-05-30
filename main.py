import datetime as dt
import pandas
import random
import smtplib
from keys import *

now = dt.datetime.now()
month = now.date().month
day_of_week = now.day

today_tuple = (month, day_of_week)

data = pandas.read_csv('birthday-test.csv')
bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in bday_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        new_letter = letter.read()
        new_letter = new_letter.replace("[NAME]", bday_dict[today_tuple]['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_sender,
            msg=f"Subject: HAPPY BIRTHDAY!\n\n{new_letter}"
            )
