'''
Write a Python program to perform the following tasks:
 Display today’s date and current time
 Display New date after 5 years and 5 days later; display new time after 4 hours later from the
current time
 Display New date after 10 years and 1 month later; display new time 4 hours and 15 minutes
earlier from the current time.
 Import a library to perform the task: import datetime
Hints: Today’s date: datetime.date.today(), Current time: datetime.datetime.now().time()
'''

import time
import datetime
import calendar
from datetime import timedelta

today = datetime.date.today()

print('~Today\'s Date~')
print("Year:",today.strftime("%Y"))
print("Month:", today.strftime("%m"))
print("Day:", today.strftime("%d"))

now = datetime.datetime.now()
print('~Current Time~')
print("Hour:", now.strftime("%H"))
print("Minute:", now.strftime("%M"))
print("Second:", now.strftime("%S"))

#get last day of the month
def last_day_of_the_month(year,month):
    y = int(year)
    m = int(month)
    num_day = calendar.monthrange(y,m)
    last_day = datetime.date(y,m, num_day[1])
    return int(last_day.strftime("%d"))
year= today.strftime("%Y")
month = today.strftime("%m")
last_day= last_day_of_the_month(year,month)

print('')
print('~New date after 5 years and 5 days later~')

#current year
current_year = today.strftime("%Y")
five_year_later = int(current_year) + 5

#current_day
current_day = today.strftime("%d")
five_day_later = int(current_day) +5

#current month
current_month = int(today.strftime("%m"))

#check if five day later is larger than max day of the month
if(five_day_later > last_day):
    five_day_later = five_day_later % last_day
    current_month +=1
    if(current_month > 12):
        current_month = current_month % 12
        five_year_later +=1

print("Year:", five_year_later)
print("Month:", current_month)
print("Day:", five_day_later)

print('~New Time: 4hours later~')
four_hour_later = now + timedelta(hours = 4)
print('Hour:',format(four_hour_later, '%H'))
print('Minute:', format(four_hour_later, '%M'))
print('Second:', format(four_hour_later, '%S'))

print('')
print('~New date after 10 years and 1 month later~')
ten_year_later = int(current_year) + 10
current_month = today.strftime("%m")
one_month_later = int(current_month) +1

#check if max month is reach
if(one_month_later > 12):
    one_month_later = one_month_later % 12
    ten_year_later += 1

print('Year:', ten_year_later)
print('Month:', one_month_later)
print('Day:', current_day)

print('~New time: 4 hour and 15 minutes earlier~')
new_time = now - timedelta(hours=4,minutes=15)
print('Hour:', format(new_time, "%H"))
print('Minute:', format(new_time, "%M"))
print('Second', format(new_time, "%S"))
