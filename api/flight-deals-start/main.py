#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from notification_manager import NotificationManager
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

notificationManager = NotificationManager()
flightSearch = FlightSearch()
flightData = FlightData()
dataManager = DataManager()


data = dataManager.get_data()
# print(data)
# print("\n\n\n\nafter\n\n")
for i in range(len(data)):
    if len(data[i]["iataCode"]) == 0:
        data[i]["iataCode"] = flightSearch.location(data[i]["city"])
        p = {
            'sheet1':data[i]
        }
        dataManager.update_data(i+2,p)
    fly_from = "DEL"
    fly_to = data[i]["iataCode"]
    payload = flightData.search_payload(fly_from, fly_to)
    try:
        search_results = flightSearch.search(payload)
        print(search_results)
    except IndexError:
        print(f"No flights found for {data[i]['iataCode']}.")
        break
    if search_results["data"][0]["price"] <= data[i]["lowestPrice"]:
        notificationManager.tg_bot(data[0]["lowestPrice"],search_results["data"][0]["price"],search_results["data"][0]["route"][0]["local_departure"].split("T")[0],search_results["data"][0]["route"][1]["local_departure"].split("T")[0])