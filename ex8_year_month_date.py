import datetime

currentDateTime = datetime.datetime(2022, 7, 25)
print(currentDateTime)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
print("Year - ", year(currentDateTime))
print("Month - ", month(currentDateTime))
print("Day - ", day(currentDateTime))
