from calendar import weekday
import calendar
import sys

def check_season(month):
    if month <= 3 and month > 0:
        result = 'Spring'
    elif month >3 and month <=6:
        result = 'Summer'
    elif month > 6 and month <=9:
        result = 'Autumn'
    elif month > 9 and month <=12:
        result = 'Winter'

    return result

print('Know more about your birthday!')
print('1. Find your birthday\'s day')
print('2. Find your birthday\'s day, n years later (based on user input)')
print('3. Find the season based on your birthday date')
print('4. Find your birthday\'s day, after n age (based on user input)')

selection = input('Selection:')

if selection == '1':
    try:
        date = input('Enter a date in YYYY/MM/DD format:')
        date_list = date.split('/')
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])

        weekday = weekday(year,month,day)
        print('Your birthday\'s day is: %s'%(calendar.day_name[weekday]))
    except ValueError:
        print('Wrong input.')
        sys.exit(1)
elif selection == '2':
    try:
        date = input('Enter a date in YYYY/MM/DD format:')
        date_list = date.split('/')
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])

        later_year = int(input('n Years Later:'))
        new_year = later_year+year
    
        weekday = weekday(new_year,month,day)
        print('In year %i Your birthdayt\'s day is: %s'%(new_year, calendar.day_name[weekday]))
    except ValueError:
        print('Wrong input.')
        sys.exit(1)
elif selection == '3':
    try:
        date = input('Enter a date in YYYY/MM/DD format:')
        date_list = date.split('/')
        month = int(date_list[1])
        result = check_season(month)

        print('Your birth season is: %s'%(result))
    except ValueError:
        print('Wrong input.')
        sys.exit(1)
elif selection == '4':
    try:
        date = input('Enter a date in YYYY/MM/DD format:')
        date_list = date.split('/')
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])

        age = int(input('Age:'))
        year_age = age + year

        weekday = weekday(year_age,month,day)
        print('When you are %i years old your birthday\'s day is: %s'%(age, calendar.day_name[weekday]))
    except ValueError:
        print('Wrong input.')
        sys.exit(1)
