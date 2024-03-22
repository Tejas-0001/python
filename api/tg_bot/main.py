import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/sraj2/PycharmProjects/python/codes angela/api/environment variables/.env")

def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("TG_BOT_TOKEN")
    bot_chatID = os.getenv("TG_BOT_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Testing Telegram bot ehehehhe env ")
print(test)