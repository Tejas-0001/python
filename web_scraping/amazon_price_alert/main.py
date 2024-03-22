from bs4 import BeautifulSoup
import requests
import smtplib
r = requests.get(url="https://www.amazon.in/iQOO-Storage-Snapdragon%C2%AE-Independent-Flagship/dp/B07WHRBD95/ref=zg_bs_g_1805560031_sccl_23/258-7582396-2142524?th=1")
print(r)
content = r.text
# with open("website.html") as f:
#     content = f.read()

soup = BeautifulSoup(content,"html.parser")

curr_price = soup.find("span",class_="a-price-whole").text.split(".")[0]
t = curr_price.split(",")
curr_price = int(''.join(t))
print(curr_price)

email = "sraj28383@gmail.com"
password = "nwrbqjvjqmyzxkcj"
rec = "sillystopapupa@gmail.com"

if curr_price <35000:
    connection = smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs=rec,msg=f"subject:price drop alert\n\niqoo neo 7 pro is available now for {curr_price}")
    connection.close()