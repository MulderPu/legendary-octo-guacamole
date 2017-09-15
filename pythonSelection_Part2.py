'''
Write a Python program for Google Grocery shop to ease their cashiers to return the cash to their
customers.
'''
import sys

print('Google Grocery Shop')
print('[V]egetable selection')
print('[M]eat selection')
print('[S]eafood selection')

def calculate_vegetable (cabbage=0,french_bead=0,brinjal=0,broccoli=0):
    cabbage_price = float(2.30)
    french_per_gram = float(1.50)
    brinjal_per_gram = float(1.20)
    broccoli_price = float(1.80)

    result = (cabbage*cabbage_price)+(french_bead*french_per_gram)+(brinjal*brinjal_per_gram)+(broccoli_price*broccoli)
    return result

print()
selection = input('Enter your selection:')
if selection in ['v', 'V']:
    print('Vegetable Selection')
    try:
        cabbage = int(input('Cabbage:'))
    except ValueError:
        cabbage = 0

    try:
        french_bead = int(input('French bead:'))
    except ValueError:
        french_bead = 0

    try:
        brinjal = int(input('Brinjal:'))
    except ValueError:
        brinjal = 0

    try:
        broccoli = int(input('Broccoli'))
    except ValueError:
        broccoli = 0
    total = calculate_vegetable(cabbage,french_bead,brinjal,broccoli)
    print('Total:',total)
elif selection in ['m', 'M']:
    print('meat')
elif selection in ['s', 'S']:
    print('seafood')
else:
    print('Wrong input. Please try again.')
    sys.exit(1)

print()
try:
    amount_paid = float(input('Amount Paid:'))
except ValueError:
    amount_paid = 0

changes = amount_paid - total
print('Change:',changes)

