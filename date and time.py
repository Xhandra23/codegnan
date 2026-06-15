'''
#date and time
--------------
-->python provides the built-in datetime module to work with dates and
time
import datetime
--------------
import datetime
d=datetime.date.today()
n=datetime.datetime.now()
print(d)
print(n)
print(f"this year: {n.year}")
print(f"month :{n.month}")
print(f"day :{n.day}")
print(f"hours:{n.hour}")
print(f"mintues:{n.minute}")
print(f"second:{n.second}")

formattting date and time
-------------------------
--> strftime() is used to formate date and time
%d --> day
%m --> month
%Y-->year




import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))

timedelta
---------

import datetime
today = datetime.date.today()
future= today + datetime.timedelta(days = 45)
print(future)

import datetime
day = datetime.date.today()
print(day.weekday())
print(day.ctime())
print(day.strftime(" %m-%d"))
'''
import calendar
year= 2027
month =11
#print(calendar.month(year,month))
print(calendar.calendar(year))

























