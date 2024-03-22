import requests,os
from dotenv import load_dotenv

load_dotenv("../environment variables/.env")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.key = os.getenv("TG_BOT_TOKEN")
        self.id = os.getenv("TG_BOT_CHAT_ID")
        self.message = "🥳🥳Price for flight from delhi to astana is lower than avg price of "


    def tg_bot(self,avg,price,datej,dater):
        url = "https://api.telegram.org/bot" + self.key + "/sendMessage?chat_id=" + self.id +"&parse_mode=Markdown&text=" + f"{self.message}{avg}\nCurrent price is : Rs{price} 👀\nDate of journey :{datej} 🤩\nDate of return : {dater}😭"
        r = requests.get(url)
        return r.json()