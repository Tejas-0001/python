import pandas
data = pandas.read_csv("Squirrel_Data.csv")
g = data[data["Primary Fur Color"] == "Gray"]
r = data[data["Primary Fur Color"] == "Cinnamon"]
b = data[data["Primary Fur Color"] == "Black"]
g_no = g["Primary Fur Color"].count()
r_no = r["Primary Fur Color"].count()
b_no = b["Primary Fur Color"].count()
# d = {
#     "grey": g_no,
#     "red": r_no,
#     "black": b_no
# }
                                        # if using all scalars you need to do 1 of the following
                                        # -- pass and index = [0] in dataframe
                                        # convert all scalar item in list by wrapping inside [] the scalar value
# t = pandas.DataFrame(d,index=[0])

d =  {
    "Fur color": ["grey","red","black"],
    "Count": [g_no,r_no,b_no]
}

t = pandas.DataFrame(d)
t.to_csv("new.csv")