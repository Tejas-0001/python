import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.r = None
        self.data = None
        self.header = {
            "Authorization": "Bearer tejasissilly"
        }
#         self.payload = {
#     'sheet1':
#     {
#       'city': 'Town',
#       'iataCode': '1244',
#       'lowestPrice': '378',
#     }
# }
        self.url = "https://api.sheety.co/b0ba339b6877ffbe36af879101c607d7/flightDeal/sheet1"

    def get_data(self):
        self.r = requests.get(url=self.url,headers=self.header)
        self.data = self.r.json()["sheet1"]
        return self.data

    def post_data(self,payload):
        self.r = requests.post(url=self.url,json=payload,headers=self.header)
        # print(self.r.status_code)
        # print(self.r.json())

    def update_data(self,obj_id,d):
        self.r = requests.put(url=f"{self.url}/{obj_id}",json=d,headers=self.header)
        # print(self.r.status_code)
        # print(self.r.json())
        # print(self.r.text)


# obj = DataManager()
# d={
#     'sheet1':
#     {
#       'city': 'Town',
#       'iataCode': '1244',
#       'lowestPrice': '378',
#     }
# }
# obj.post_data(d)

# obj.update_data(2,d)
# print(obj.get_data())