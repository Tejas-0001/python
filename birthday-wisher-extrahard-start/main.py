##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import random,smtplib,pandas
import datetime as dt

email = "sraj28383@gmail.com"
password = "nwrbqjvjqmyzxkcj"
rec = "sillystopapupa@gmail.com"

n = random.randint(1,3)
with open(f"./letter_templates/letter_{n}.txt") as f:
    letter = f.read()

now = dt.datetime.now()
tday = now.day
tmonth = now.month

data = pandas.read_csv("birthdays.csv")
for entry in data.iterrows():
    if tday == entry[1].day and tmonth == entry[1].month:
        t = letter.replace("[NAME]",entry[1]["name"])
        connection = smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email, to_addrs=rec,msg=f"subject:Happy Birthday\n\n{t}")
        connection.close()

