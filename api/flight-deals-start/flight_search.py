import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.key = "ahBTg6a5uJymzwOYZStbOwqPiC7Wvw1D"
        self.loc_payload = {
            "term":None,
            "location_types":"city",
        }
        self.location_url = "https://api.tequila.kiwi.com/locations/query"
        self.search_url = "https://api.tequila.kiwi.com/v2/search"
        self.header = {
            "Content - Type": "application / json",
            "apikey": self.key,
            "Content - Encoding": "gzip"
        }

    def location(self,term):
        self.loc_payload["term"] = term
        r = requests.get(url=self.location_url,params=self.loc_payload,headers=self.header)
        return r.json()["locations"][0]["code"]

    def search(self,parameters):
        r = requests.get(url=self.search_url,params=parameters,headers=self.header)
        return r.json()

    #
    # def payload(self,fly_from,fly_to,date_from,date_to):
    #     p = {
    #         "fly_from":fly_from,
    #         "fly_to":fly_to,
    #         "date_from":"07/07/2023",
    #         "date_to":"07/08/2023"
    #     }
    #     return p

# obj = FlightSearch()
# p = {
#             "fly_from":"PAR",
#             "fly_to":"TYO",
#             "date_from":"07/07/2023",
#             "date_to":"07/08/2023"
#         }
# print(obj.search(p))
