import pandas
data = pandas.read_csv("50_states.csv")
t = data[data["state"] == "0hio"]
if not t.empty:
    print(t["state"].item())
else:
    print("nothingggg")


# t = data[data["state"] == user]
# x = t["x"].item()       #method to access data in series
# y = t.y.item()
# print(x)