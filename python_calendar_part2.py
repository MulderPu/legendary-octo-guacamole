import sys
from calendar import weekday
import calendar
import time
import datetime
import calendar
from datetime import timedelta

def print_selection():
    print('[C] Show new calendar after n years (user input)')
    print('[D] Show new date based on user input')
    print('[T] Show new time based on user input')


print('Month, time, day')
print('[A] To calculate new calendar based on current date & time')
print('[B] To calcualte new calendar based on user input (date & time)')

selection = input('Selection:')


today = datetime.date.today()

try:
    if selection in ['a', 'A']:
        print_selection()
        selection_2 = input('Selection:')

        if selection_2 in ['c','C']:
            print('Show new calendar after n years (user input)')
            
            try:
                input_years = int(input('Years:'))
                year = int(today.strftime("%Y"))
                month = int(today.strftime("%m"))
                day = int(today.strftime("%d"))

                new_year = year+input_years
                print('%i-%i-%i'%(new_year,month,day))
                weekday = weekday(year,month,day)
                print('Day: %s'%(calendar.day_name[weekday]))

            except ValueError:
                print('Integer only.Please try again.')
                sys.exit(1)
            




except ValueError:
    print('Wrong input.')
    sys.exit(1)
