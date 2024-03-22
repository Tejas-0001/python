import random,datetime,smtplib
email = "sraj28383@gmail.com"
password = "nwrbqjvjqmyzxkcj"
rec = "sillystopapupa@gmail.com"

with open("quotes.txt") as f:
    data = f.readlines()
quote = random.choice(data)

now = datetime.datetime.now()
tday = now.weekday()

if tday == 5:
    connection = smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs=rec,msg=f"subject:Motivation quote\n\n{quote}")
    connection.close()
else:
    print("aint tno way")
