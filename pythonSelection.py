'''
Write a Python program to accept an input for “selection” the input can accept either upper case or
lower case, and input for the amount.
Calculate the total based on the selection and amount input.
'''
import sys
import locale

locale.setlocale(locale.LC_ALL, '')

def convertToMYR(number):
    number = locale.currency(number).replace('$', 'MYR ')
    return number

print('B & B Inn')
print('Breakfast Selection:')
print('[A]merican Breakfast (RM12.50)')
print('[C]hinese Porridge   (RM 6.30)')
print('[N]asi Lemak         (RM 5.50)')
print('[F]ried Noodle       (RM 5.50)')
print('[L]aksa              (RM 5.30)')
print('[M]ee mamak          (RM 4.80)')
print()
selection = input('Enter your selection:')

if (selection.isalpha()):
    number = input('Enter the amount:')
    if(number.isdigit()):
        if selection in ['a', 'A']:
            result = int(number)*12.50
        elif selection in ['C', 'c']:
            result = int(number)*6.30
        elif selection in ['N', 'n']:
            result = int(number)*5.50
        elif selection in ['F', 'f']:
            result = int(number)*5.50
        elif selection in ['L', 'l']:
            result=int(number)*5.30
        elif selection in ['M', 'm']:
            result = int(number)*4.80
        else:
            print('Your selection is not on menu. Please select again.')
            sys.exit(1)
        print('Total:',convertToMYR(result))
    else:
        print('Please enter number only.')
        sys.exit(1)
else:
    print('Selection must be alphabet only. Please try again.')
    sys.exit(1)

