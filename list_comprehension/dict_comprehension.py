# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # words = sentence.split()
# d = {word:len(word) for word in sentence.split()}
# print(d)


# big = {key:value for (key,value) in d.items() if value>6}
# print(big)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {key:value*9/5 + 32 for (key,value) in weather_c.items()}
# print(weather_f)



import pandas
student_dict = {
    "student": ["angela","james","Lily"],
    "score":[56,76,98]
}

d = pandas.DataFrame(student_dict)

# # loop through data frame
# for (key,value) in d.items():
#     print(value)

#loop through row of dataframe
for (index,row) in d.iterrows():
    # print(row)
    print(row.student)
    print(row["score"])