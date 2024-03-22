import smtplib
import requests
from datetime import datetime
import time

EMAIL = "sraj28383@gmail.com"
PASSWORD = "nwrbqjvjqmyzxkcj"

MY_LAT = 20.593683 # Your latitude
MY_LONG = 78.962883 # Your longitude

while 1:

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    flag = False
    if 5>MY_LAT-iss_latitude>-5 and 5>MY_LONG-iss_longitude:
        flag = True
    else:
        print("ISS is not near")


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    #If the ISS is close to my current position


    if flag is True:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        if time_now.hour > sunset or time_now.hour < sunrise:
            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(EMAIL,PASSWORD)
                connection.sendmail(from_addr=EMAIL,to_addrs = "sillystopapupa@gmail.com",msg="Subject:ISS is overhead you now\n\nLook in the sky")
        else:
            print("it's daytime you can't see iss")
    time.sleep(60)

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



