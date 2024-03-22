STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
import os
from datetime import date,timedelta

today = date.today()
yesterday = today - timedelta(days=4)
y_yesterday = today- timedelta(days=5)
today = str(today)
yesterday = str(yesterday)
y_yesterday = str(y_yesterday)



from dotenv import load_dotenv
load_dotenv("./../../environment variables/.env")

parameter = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "outputsize":"compact",
    "datatype":"json",
    "apikey":os.getenv("STOCK")
}

response = requests.get(url="https://www.alphavantage.co/query",params=parameter)
data = response.json()["Time Series (Daily)"]
print(data)
data_y = float(data[f"{yesterday}"]["4. close"])
data_y_y = float(data[f"{y_yesterday}"]["4. close"])

temp = (data_y-data_y_y)/data_y_y


def tg_bot(bot_message):
    bot_token= os.getenv("TG_BOT_TOKEN")
    bot_chat_id = os.getenv("TG_BOT_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
    res = requests.get(send_text)
    print(res.json())


if temp > 0.05:
    print("news time")
    r = requests.get(url=f"https://newsapi.org/v2/everything?q=tesla&from=2023-06-03&sortBy=publishedAt&apiKey={os.getenv('NEWS_TESLA')}")
    d = r.json()["articles"]
    t = [(d[i]["title"],d[i]["description"]) for i in range(3)]
    for items in t:
        msg = f"{STOCK}: 🔺{round(temp*100)}%\nHeadline: {items[0]}.\nBrief: {items[1]}."
        tg_bot(msg)


elif temp < -0.05:
    print("news time")
    r = requests.get(
        url=f"https://newsapi.org/v2/everything?q=tesla&from=2023-06-03&sortBy=publishedAt&apiKey={os.getenv('NEWS_TESLA')}")
    d = r.json()["articles"]
    t = [(d[i]["title"], d[i]["description"]) for i in range(3)]
    for items in t:
        msg = f"{STOCK}: 🔻{round(temp * 100)}%\nHeadline: {items[0]}.\nBrief: {items[1]}."
        tg_bot(msg)
else:
    print("mehhh")
