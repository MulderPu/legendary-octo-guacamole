import sys
from calendar import weekday
import calendar
import datetime
from dateutil.relativedelta import relativedelta

def print_selection():
    print('[C] Show new calendar after n years (user input)')
    print('[D] Show new date based on user input')
    print('[T] Show new time based on user input')

def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

def get_input_date():
    input_date = input('Enter a date in YYYY/MM/DD format:')
    dt_start = datetime.datetime.strptime(input_date, '%Y/%m/%d') 
    return dt_start

def get_input_time():
    input_time = input('Enter a time in hh:mm:ss format:')
    time_start = datetime.datetime.strptime(input_time, '%H:%M:%S')
    return time_start

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
        elif selection_2 in ['d','D']:
            print('Show new date based on user input')

            try:
                input_days = int(input('Days:'))

                date_after = today + relativedelta(days=input_days) 
                print(date_after)
                year = int(date_after.strftime("%Y"))
                month = int(date_after.strftime("%m"))
                day = int(date_after.strftime("%d"))

                weekday = weekday(year,month,day)
                print('Day: %s'%(calendar.day_name[weekday]))
            except ValueError:
                print('Integer only.Please try again.')
                sys.exit(1)

        elif selection_2 in ['t','T']:
            print('Show new time based on user input')

            try:
                input_hour = int(input('Hours:'))
                input_mins = int(input('Minutes:'))
                input_sec = int(input('Seconds:'))

                current_time =datetime.datetime.now().time() 
                print('Current time: %s'%(current_time))

                hour_to_sec = input_hour * 3600
                mins_to_sec = input_mins * 60 
                total_sec = hour_to_sec + mins_to_sec + input_sec
                new_time = addSecs(current_time,total_sec)
                print('New time is: %s'%(new_time))
            except ValueError:
                print('Wrong input.Please try again.')
                sys.exit(1)
    elif selection in ['b','B']:
        print_selection() 
        selection_2 = input('Selection:')

        if selection_2 in ['c','C']:
            print('Show new calendar after n years (user input)')
            
            try:
                dt_start = get_input_date()

                input_years = int(input('Years:'))
                year = int(dt_start.strftime("%Y"))
                month = int(dt_start.strftime("%m"))
                day = int(dt_start.strftime("%d"))

                new_year = year+input_years
                print('%i-%i-%i'%(new_year,month,day))
                weekday = weekday(year,month,day)
                print('Day: %s'%(calendar.day_name[weekday]))

            except ValueError:
                print('Integer only.Please try again.')
                sys.exit(1)
        elif selection_2 in ['d','D']:
            print('Show new date based on user input')

            try:
                input_date = get_input_date()
                input_days = int(input('Days:'))

                date_after = input_date + relativedelta(days=input_days) 
                print(date_after.strftime('%Y/%m/%d'))
                year = int(date_after.strftime("%Y"))
                month = int(date_after.strftime("%m"))
                day = int(date_after.strftime("%d"))

                weekday = weekday(year,month,day)
                print('Day: %s'%(calendar.day_name[weekday]))
            except ValueError:
                print('Integer only.Please try again.')
                sys.exit(1)

        elif selection_2 in ['t','T']:
            print('Show new time based on user input')

            try:
                input_time = get_input_time()
                time = input_time.strftime('%H:%M:%S')

                input_hour = int(input('Hours:'))
                input_mins = int(input('Minutes:'))
                input_sec = int(input('Seconds:'))

                print('Current time: %s'%(time))

                hour_to_sec = input_hour * 3600
                mins_to_sec = input_mins * 60 
                total_sec = hour_to_sec + mins_to_sec + input_sec
                new_time = addSecs(input_time,total_sec)
                print('New time is: %s'%(new_time))
            except ValueError:
                print('Wrong input.Please try again.')
                sys.exit(1)

except ValueError:
    print('Wrong input.')
    sys.exit(1)
