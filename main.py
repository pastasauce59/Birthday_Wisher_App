import datetime as dt
import pandas
import random

now = dt.datetime.now()
month = now.date().month
day_of_week = now.day

today_tuple = (month, day_of_week)

data = pandas.read_csv('birthday-test.csv')
# print(data)
bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# print(bday_dict)

if today_tuple in bday_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        new_letter = letter.read()
        print(new_letter.replace("[NAME]", bday_dict[today_tuple]['name']))