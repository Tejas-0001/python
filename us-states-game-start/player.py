import pandas
# data = pandas.read_csv("50_states.csv")
# user = "ohio".capitalize()
# t = data[data["state"] == user]
# x = t["x"].item()       #method to access data in series
# y = t.y.item()

class Player:

    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.guessed = []
        self.user = ""
        self.guessed_count = 0
        self.total_count = len(self.data)

    def guess(self,g):
        self.user = g.capitalize()
        if self.user not in self.guessed:
            t = self.data[self.data["state"] == self.user]
            if not t.empty:
                self.guessed.append(t["state"].item())
                x = t["x"].item()  # method to access data in series
                y = t.y.item()
                self.guessed_count += 1
                return g, x, y
            else:
                return "this country is not present in USA"
        elif self.user in self.guessed:
            return "Already Guessed"

    def game_over(self):
        state = self.data.state.to_list()
        for item in state:
            if item in self.guessed:
                state.remove(item)
        temp = pandas.DataFrame(state)
        temp.to_csv("state_left.csv")

