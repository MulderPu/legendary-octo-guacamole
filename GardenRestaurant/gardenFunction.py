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

def validateVenue(choice, venueList, noPeople):
    return False
