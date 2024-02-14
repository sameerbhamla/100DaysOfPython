##################### Normal Starting Project ######################
from datetime import datetime
import pandas
from random import randint
import smtplib

MY_EMAIL = 'bhamlasameer@gmail.com'
MY_PASSWORD = 'evowdpngiohacsqz'
# 1. Update the birthdays.csv with your friends & family's details.

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'letter_templates/letter_{randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]',birthday_person['name'])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject:Happy Birthday!\n\n'
                                f'{contents}')

