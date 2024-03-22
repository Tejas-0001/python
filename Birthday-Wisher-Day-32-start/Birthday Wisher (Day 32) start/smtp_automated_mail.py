import smtplib
email = "sraj28383@gmail.com"
password = "nwrbqjvjqmyzxkcj"

rec = "sillystopapupa@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=email,password=password)
connection.sendmail(from_addr=email, to_addrs=rec,msg="subject:learning\n\nwowowowoowoow!!!")
connection.close()