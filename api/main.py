import requests
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() #it gives the response status code error
# data = response.json()    -> this is now a python dictionary
data = response.json()["iss_position"]
long = data["longitude"]
lati = data["latitude"]

parameter = {
    "lng":long,
    "lat":lati,
    "formatted":0
}
# print(parameter)

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sr= data["results"]["sunrise"].split("T")[1].split(":")[0]     #-> time in hours
ss= data["results"]["sunset"].split("T")[1].split(":")[0]
# temp = sr.split("T")
# print(temp[1].split(":"))
print(sr)
print(ss)

tday = dt.datetime.now()
print(tday.hour)