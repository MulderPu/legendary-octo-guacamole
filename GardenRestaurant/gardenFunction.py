import datetime

'''
Get list of data from text file

@param {txt}
@return {list}
'''
def readVenueList(textFile):
    list = []

    with open(textFile,"r") as text:
        for line in text:
            items = line.split(',')
            dict = {}
            dict['name'] = items[0]
            dict['max']  = items[1].strip()
            dict['cost'] = items[2].strip(' ').strip('\n')
            list.append(dict)
    return list

'''
Validate customer name
Must have surname and given name
No numbers allowed

@param {string}
@return {bool}
'''
def validateCustomerName(name):
    if (name != "") and (len(name.split(' ')) == 2):
        list= name.split(' ')
        for i in list:
            if not i.isalpha():
                return False
        return True
    return False

'''
Validate number of people
Must not empty
Must be digit
Must > 1
Must < 1000

@param  {String}   
@return {int}        
'''
def validateNoOfPeople(people):
    if (people.isdigit()) and (int(people) > 1) and (int(people) < 1000):
        return int(people)
    return -1

'''
Validate phone number
Must equal 10
Must not empty
Must be digit
'''
def validatePhoneNumber(number):
    if (number.isdigit()) and (len(number) == 10) and (number != ''):
        return number
    return -1

'''
Validate if venue selected can fit in the number of people
'''
def validateVenue(choice, venueList, noPeople):
    i = choice-1
    max_capacity = venueList[i]['max']
    if( int(noPeople) < int(max_capacity)):
        return True
    return False

'''
Read file and return data in list
'''
def readItemList(textFile):
    list = []
    with open(textFile,"r") as text:
        for line in text:
            if line.strip('\n') != '':
                list.append(line.strip('\n'))
    return list

'''
Calculate total tables needed based on number of people
'''
def calculateTableTotal(noPeople):
    table_count = 0
    remainding = int(noPeople % 10)
    table_count = int(noPeople / 10)
    if remainding < 6 and table_count > 1:
        table_count -= 1
    return table_count

'''
Calculate venue price based on venue chosen
'''
def calculateVenuePrice(venueChoice):
    list = [{'name': 'VIP ROOM (10 persons)', 'cost': 'FREE'},
            {'name': 'Executive Room (30 persons)', 'cost': 'FREE'},
            {'name': 'Pool site (50 persons)', 'cost': '800.00'},
            {'name': 'Banquet Hall (200 persons)', 'cost': '1000.00'},
            {'name': 'Chamber Hall (500 persons)', 'cost': '1500.00'},
            {'name': 'Concert Hall (1000 persons)', 'cost': '1800.00'}
            ]
    for i in range(len(list)):
        if venueChoice-1 == i:
            return list[i]
    return []

'''
Calculate the total menu price based on the choice and number of table
'''
def calculateMenuPrice(totalTable, choice):
    list = [
        {'name': 'Menu 1', 'cost' : '768.88'},
        {'name': 'Menu 2', 'cost' : '898.88'},
        {'name': 'Menu 3', 'cost' : '1118.88'},
        {'name': 'Menu 4', 'cost' : '1488.88'}
    ]

    price = 0
    menu = ''
    for i in range(len(list)):
        if choice-1 == i:
            price = list[i]['cost']
            menu = list[i]['name']
    total_menu_price = int(totalTable) * float(price)
    print(total_menu_price)
    print(menu)
    
    return {'total_price': total_menu_price, 'selected_menu': menu}

    
'''
Calculate entertainments price
'''
def calculateEntertainment(choice, venueChoice):
    list = [
        {'entertainments':'Synchronised Swimming Dance', 'Availability':'Pool', 'cost':'2000'},
        {'entertainments':'Clown Performance', 'Availability':'Pool , Banquet Hall, Chamber Hall, Concert Hall', 'cost':'250'},
        {'entertainments':'Magic Performance', 'Availability':'Pool, Banquet Hall, Chamber Hall, Concert Hall', 'cost':'450'},
        {'entertainments':'House Dance Performance', 'Availability':'Banquet Hall, Chamber Hall, Concert Hall', 'cost':'1000'},
        {'entertainments':'Live Band Performance', 'Availability':'Banquet Hall, Chamber Hall, Concert Hall', 'cost':'1500'},
    ]

    cost=0
    entertainments=''
    for i in range(len(list)):
        if choice-1 == i:
            cost=list[i]['cost']
            entertainments = list[i]['entertainments']

    return {'price':cost, 'entertainments':entertainments}


'''
Calculate total price
'''
def calculateTotalPrice(venuePrice, menuPrice, entertainmentPrice):
    return int(venuePrice)+int(menuPrice)+int(entertainmentPrice)

'''
Save booking details into text file
'''
def booking(custName,custNo,noPeople,totalTable,strVenue,strMenu,strEntertainment, total):
    #today date
    now = datetime.datetime.now()
    todayDate= now.strftime("%Y%m%d")
    
    #file name
    filename = 'Garden/booking/'+custName + '_' + todayDate+'.txt'
    with open(filename, "w") as text_file:
        text_file.write("Your reservation has been confirmed.")
        
        text_file.write("\n------------------------------------")
        text_file.write("\nBooking Summary")
        text_file.write("\n------------------------------------")

        text_file.write("\nCustomer Name: %s" % (custName))
        text_file.write("\nContact Number: %s" % (custNo))
        text_file.write("\nNo of People: %s" % (noPeople))
        text_file.write("\nTables: %s" % (totalTable))
        text_file.write("\nVenue: %s" % (strVenue))
        text_file.write("\nPackage: %s" % (strMenu))
        text_file.write("\nAdd on: %s" % (strEntertainment))
        text_file.write("\nTotal Price: %s" % (total))

