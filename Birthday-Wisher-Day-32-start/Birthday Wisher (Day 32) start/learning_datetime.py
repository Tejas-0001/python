import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
print(month)

day = now.day
print(day)

week_day = now.weekday()
print(week_day)

dob = dt.datetime(year=2002,month=1,day=25)
print(dob)