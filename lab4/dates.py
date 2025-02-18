
#1 
import datetime

current_date = datetime.datetime.now()


new_date = current_date - datetime.timedelta(days=5)
print("date without 5 days:", new_date)



#2
import datetime


today = datetime.datetime.now()


yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)


print("yesterday:", yesterday)
print("today:", today)
print("tomorrow:", tomorrow)



#3
import datetime


current_datetime = datetime.datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)


print("current datetime:", current_datetime)
print("datetime without microseconds:", datetime_without_microseconds)



#4
import datetime
import math


date1 = input("first date (format YYYY-MM-DD HH:MM:SS): ")
date2 = input("second date (format YYYY-MM-DD HH:MM:SS): ")


date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")


difference = abs(date2 - date1)  

print( difference.total_seconds())
