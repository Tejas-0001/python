import requests
import datetime
user = "tej"
password = "tejas"


# r = requests.get(url="https://api.sheety.co/b0ba339b6877ffbe36af879101c607d7/copyOfMyWorkouts/workouts")
# print(r.json())

today = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")
# print(today)
# print(time)
#
p={"workout":{
    "workouts":[{
        "date":today,
        "time":time,
        "exercise":"running",
        "duration":"22",
        "calories":"130",
        "id":"6"
    }]}
}

# header = {
# "Authorization": "Basic dGVqOnRlamFz"
# }

header={
"Authorization": "Bearer dfaa32y682y6dgszzbhzb"
}


# {'workouts': [{'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2}]}

r = requests.post(url="https://api.sheety.co/b0ba339b6877ffbe36af879101c607d7/copyOfMyWorkouts/workouts",json=p,headers=header)
print(r.json())