import datetime
import gardenFunction

'''
Header of the program
'''
def printBanner():
    print("*"*40)
    print("|" +" "*38+"|")
    print("|"+ " "*10 + "Garden Restaurant"+" "*10 +" |")
    print("|" +" "*38+"|")
    print("*"*40)

    print()
    print('Welcome to Garden Restaurant Booking Management System.')
    
    #today date
    now = datetime.datetime.now()
    todayDate= now.strftime("%Y-%m-%d")
    print('Today\'s Date: %s' % todayDate)

'''
List of venue
'''
def printVenue():
    print("-"*40)
    print('Venue')
    print("-"*40)

    print()
    filename = 'Garden/venue.txt'
    list = gardenFunction.readVenueList(filename)

    for i in range(len(list)):
        count = i +1
        name = list[i]['name']
        people = list[i]['max']
        print('[' + str(count) + ']' + ' ' + name + ' ('+people+' persons)')

'''
List of menu package
'''
def printMenuPackage():
    print('-'*40)
    print('Menu Option')
    print('-'*40)
    print()
    print('[1] RM768.88 Package \t[3] RM1118.88 Package')
    print('[2] RM898.88 Package \t[4] RM1488.88 Package')

'''
Show menu list based on menu chosen
'''
def printPackage(menuList):
    print('-'*40)
    print('Menu List')
    print('-'*40)
    print()
    filename = "Garden/menu/Menu"+str(menuList)+".txt"

    #read file
    list = gardenFunction.readItemList(filename)

    for i in range(len(list)):
        count = i + 1
        print(str(count)+' . '+list[i])

    result = input('Is the selected menu okay? \n[1] Yes\n[2] No, I want to reselect my menu\n')
    if(result == '2'):
        return False
    else:
        return True


def printEntertainment(venueChoice,entertainmentList,venueList):
    print('Entertainment for Pool Site')
    print(entertainmentList)


venueList = gardenFunction.calculateVenuePrice(4)
entertainmentList= [
        {'entertainments':'Synchronised Swimming Dance', 'Availability':'Pool', 'cost':'2000'},
        {'entertainments':'Clown Performance', 'Availability':'Pool , Banquet Hall, Chamber Hall, Concert Hall', 'cost':'250'},
        {'entertainments':'Magic Performance', 'Availability':'Pool, Banquet Hall, Chamber Hall, Concert Hall', 'cost':'450'},
        {'entertainments':'House Dance Performance', 'Availability':'Banquet Hall, Chamber Hall, Concert Hall', 'cost':'1000'},
        {'entertainments':'Live Band Performance', 'Availability':'Banquet Hall, Chamber Hall, Concert Hall', 'cost':'1500'},
    ]
list_name = venueList['name'].split(' ')
name = list_name[0]
list_entertainment = []
for i in entertainmentList:
    available =  i['Availability'].lower().split(',')
    for j in available:
        if name.lower() in j:
            list_entertainment.append(i['entertainments'])
#printEntertainment(1, list_entertainment, venueList)
