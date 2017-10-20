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
    choice = input('\n\nPlease select a venue:')
    if choice in ['1','2','3','4','5','6']:
        #validate venue
        status_venue = gardenFunction.validateVenue(choice, venueList, no_of_people)
        if status_venue == True:
            flag=0
        else:
            print('Sorry, number of people exceed venue max capacity.\nPlease choose again.')
            flag=1
    else:
        print('Invalid venue, please choose again.')
        flag=1
print(choice)
