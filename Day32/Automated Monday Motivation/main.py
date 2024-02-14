import random
import smtplib
import datetime as dt

my_email = 'bhamlasameer@gmail.com'
password = 'evowdpngiohacsqz'
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='bhamlasameer@yahoo.com',
            msg=f'Subject: Monday Motivation\n\n'
                f'{quote}'
        )
