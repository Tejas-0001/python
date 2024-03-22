from datetime import timedelta,date
class FlightData:

    def __init__(self):
        x = date.today()
        self.date = x.strftime("%d/%m/%Y")
        self.date_from = x + timedelta(days=120)
        self.date_to = x + timedelta(days=125)
        self.return_from = x + timedelta(days=138)
        self.return_to = x + timedelta(days=140)
        self.flight_type = "round"
        # self.max_stopovers = 0
        self.curr = "INR"

    def search_payload(self,fly_from,fly_to):
        p = {
            "fly_from":fly_from,
            "fly_to":fly_to,
            "date_from":self.date_from,
            "date_to":self.date_to,
            "return_from":self.return_from,
            "return_to":self.return_to,
            "flight_type":self.flight_type,
            # "max_stopovers":self.max_stopovers,
            "curr": self.curr
        }
        return p
