'''
Write a python program for the following output.
Accept 3 values: Initial value, Ending value and Counter value for while loop.
The program be able to determine it is either an Increase loop or a Decrease loop from the values
input and display the values after the process.  If the value entered for Counter value to be a
negative value, change it to a positive value for the process.
The program will continue if “c” or “C” is enters, “x” or “X” is to exit the program
'''

i=1
while (i):
    initial = int(input('Enter Initial value:'))
    ending = int(input('Enter Ending value:'))
    print('To increase/decrease the loop')
    counter = int(input('Enter Counter value:'))

    if initial > ending:
        print('Decrease loop')

        while (initial > ending):

            initial = initial - counter
            print(initial)
    else:
        print('Increase loop')

        while (ending > initial):
            initial=initial+counter
            print(initial)

    selection = input('Enter c to continue and x to exit:')

    if selection in ['c','C']:
        i=1
    elif selection in ['x','X']:
        print('Thank You.')
        i=0

