import requests
import datetime


website = "https://pixe.la/@tejasosiily"
TOKEN = "teske43srx65eiykrxfxrrfs46rxfhyfer64y"
USERNAME = "tejasosiily"
GRAPHID = "silly"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


# r = requests.post(url=pixela_endpoint,json=user_parameters)
# print(r.text)

headers = {
    "X-USER-TOKEN":TOKEN
}

# parameters = {
#     "id":"silly",
#     "name":"walking",
#     "unit":"km",
#     "type":"float",
#     "color":"ajisai"
# }
#
#
# r = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs",json=parameters,headers=headers)
# print(r.text)


today = datetime.datetime(year=2023,month=7,day=2)
date = today.strftime("%Y%m%d")


p = {
    "date":date,
    "quantity":"10.4"
}


#
# r = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}",json=p,headers=headers)
# print(r.text)

b= {
    "quantity":"8.2"
}

# r = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}", headers=headers, json=b)
# print(r.text)

r = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}", headers=headers)
print(r.text)