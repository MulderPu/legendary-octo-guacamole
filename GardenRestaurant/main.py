import gardenFunction
import textGui

flag=1
while(flag):
    customer_name = input('Customer Name:')
    contact_no = input('Contact Number:')
    no_of_people = input('No. of people:')
    
    #validate name
    status_name = gardenFunction.validateCustomerName(customer_name)
    #validate phone
    status_phone = gardenFunction.validatePhoneNumber(contact_no)
    #validate no of people
    status_no_people = gardenFunction.validateNoOfPeople(no_of_people)

    if status_name == False:
        print('Invalid Name.')    
        flag=1
    if status_phone == -1:
        print('Invalid Phone Number.')
        flag=1
    if status_no_people == -1:
        print('Invalid no of people.')
        flag=1
    print()
    if status_name == True and status_phone != -1 and status_no_people != -1:
        flag=0

textGui.printBanner()
print()
textGui.printVenue()

#get list of venue
filename = 'Garden/venue.txt'
venueList = gardenFunction.readVenueList(filename)

flag=1
while (flag):
    venueChoice = input('\n\nPlease select a venue:')
    if venueChoice in ['1','2','3','4','5','6']:
        #validate venue
        status_venue = gardenFunction.validateVenue(venueChoice, venueList, no_of_people)
        if status_venue == True:
            flag=0
        else:
            print('Sorry, number of people exceed venue max capacity.\nPlease choose again.')
            flag=1
    else:
        print('Invalid venue, please choose again.')
        flag=1

print()
#menu list
textGui.printMenuPackage()

flag=1
while (flag):
    menuChoice = input('\n\nPlease select a menu:')
    if menuChoice in ['1','2','3','4']:
        status_menu = textGui.printPackage(menuChoice)
        if status_menu == True:
            flag=0
    else:
        print('Invalid menu, please choose again.')
        flag=1


flag=1
while (flag):
    print('\nWould you like to add on entertainment?\n[1] Yes\n[2] No')
    entertainChoice =input('Please select choice:')
    if entertainChoice in ['1', '2']:
        #do something
        flag=0
    else:
       print('Invalid choice.\n') 
       flag=1

#entertainment list
entertainmentList= [
        {'entertainments':'Synchronised Swimming Dance', 'Availability':'Pool', 'cost':'2000'},
        {'entertainments':'Clown Performance', 'Availability':'Pool , Banquet Hall, Chamber Hall, Concert Hall', 'cost':'250'},
        {'entertainments':'Magic Performance', 'Availability':'Pool, Banquet Hall, Chamber Hall, Concert Hall', 'cost':'450'},
        {'entertainments':'House Dance Performance', 'Availability':'Banquet Hall, Chamber Hall, Concert Hall', 'cost':'1000'},
        {'entertainments':'Live Band Performance', 'Availability':'Banquet Hall, Chamber Hall, Concert Hall', 'cost':'1500'},
    ]

#get entertainment choice 
entertainment_choice = textGui.printEntertainment(venueChoice, entertainmentList, venueList)
#get total number of table needed
totalTable = gardenFunction.calculateTableTotal(no_of_people)
#get price of venue selected
venuePrice = gardenFunction.calculateVenuePrice(venueChoice)
#get price of menu selected
menuPrice = gardenFunction.calculateMenuPrice(totalTable, menuChoice)

if venuePrice['cost'] == "FREE":
    venuePrice['cost'] = 0

if entertainment_choice != None:
    entertainDict = gardenFunction.calculateEntertainment(entertainment_choice, venueChoice)
    entertainPrice = entertainDict['price']
else:
    entertainPrice = 0

#get total price
totalPrice = gardenFunction.calculateTotalPrice(venuePrice['cost'], menuPrice['total_price'], entertainPrice)

if entertainPrice == 0:
    strEntertainment = '-'
else:
    strEntertainment = entertainDict['entertainments']

#show summary
textGui.printSummaryTotal (customer_name, contact_no, no_of_people, totalTable, 
                   totalPrice,venuePrice['name'], menuPrice['selected_menu'], strEntertainment)

#store booking data into text file in ./Garden/booking/
gardenFunction.booking(customer_name, contact_no, no_of_people, totalTable, venuePrice['name'],
                       menuPrice['selected_menu'], strEntertainment, totalPrice)
