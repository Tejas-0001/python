import requests

api_key = "c1fb0754f961496889e1779766636bee"

parameter={
    "lat":20.593683,
    "lon":78.962883,
    "appid":api_key
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
t = response.json()["list"]
for data in t:
    ans = data["weather"][0]["id"]
    if ans<700:
        print("it's gonna rain")
    

