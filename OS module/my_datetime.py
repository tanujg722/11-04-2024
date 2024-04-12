import datetime
mytime = datetime.time(2,20,56,3)#first hour then minutes after that seconds then microseconds

print(mytime.minute)
print(mytime.hour)
print(mytime)
print(mytime.second)
print(mytime.microsecond)

#date
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

from datetime import date
date1= date(2023,3,11)
date2= date(2024,11,3)
result = date1 - date2
print(result) # here you got the days between date1 and date2

from datetime import datetime
date1= datetime(2023,3,11,23,56)
date2= datetime(2024,11,3,12,55)
result = date1 - date2
print(result) # here you got the days between date1 and date2 and time aswell.

