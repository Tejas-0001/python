# with open("weather_data.csv") as f:
#     data = f.readlines()
#
# raw = []                                          use the library dude

# for _ in data:
#     raw.append(_.strip())
#
# print(raw)



# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     # print(data)                                 use better library dude
#     temp = []
#     for row in data:
#         temp.append(int(row[1]))
#     temp = temp[1:]
#     print(temp)




import pandas
data = pandas.read_csv("weather_data.csv")
# print(data.temp)
# data_dict = data.to_dict()
# print(data_dict)
# tmp_list = data.temp.to_list()
# print(sum(tmp_list)/len(tmp_list))
# print(data.temp.mean())
# print(data.temp.max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data.temp)
# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
# t = data[data.day == "Monday"]
# print(t.temp*9/5 + 32)



"""creating dataframes"""

d = {
    "name": ["tejas","divay","pranav"],
    "score": [21,22,23]
}

t = pandas.DataFrame(d)
# print(t)                          now store it easily in any data type
t.to_csv("learning.csv")                #write the address of file where you will save it