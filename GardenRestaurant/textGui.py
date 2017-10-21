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

    print('\nIs the selected menu okay? \n[1] Yes\n[2] No, I want to reselect my menu\n')

    flag=1
    while (flag):
        result = input('Please select a choice:')
        if result in ['1','2']:
            if result == '1':
                flag=0
                return True
            else:
                flag=0
                return False
        else:
            print('Invalid choice.')

'''
Print entertainment list based on venue choices
'''
def printEntertainment(venueChoice,entertainmentList,venueList):
    venue_name = venueList[int(venueChoice)-1]['name']
    name_list = venue_name.split(' ')
    first_venue_name =name_list[0]
    entertain_list = []
    
    for item in entertainmentList:
        entertain_available = item['Availability']
        if first_venue_name in entertain_available:
            entertain_list.append(item['entertainments'])

    if len(entertain_list) != 0:
        print('\nEntertainment for %s' % venue_name)
        count=1
        select_list = []
        for i in entertain_list:
            print(' %s %s' % (count,i))
            select_list.append(str(count))
            count += 1

        flag=1
        while (flag):
            choice = input('Please select choice:')
            if choice in select_list:
                return choice
                flag=0
            else:
                print('Invalid choice.')
    else:
        print('\nNo entertainment available for this venue.')
        return None

'''
Print Total Summary
'''
def printSummaryTotal (custName, contNum, numPeople, totalTable,
                       totalPrice, strVenue, strMenu,strEntertainment):
    print('Your reservation has been confirmed.')
    print("-"*30)
    print('Booking Summary')
    print("-"*30)
    print('Customer Name : %s' % custName)
    print('Contact Number: %s' % contNum)
    print('No of People  : %s' % numPeople)
    print('Tables        : %s' % totalTable)
    print('Venue         : %s' % strVenue)
    print('Package       : %s' % strMenu)
    print('Add on        : %s' % strEntertainment)
    print()
    print('Total Price   : %s' % totalPrice)
