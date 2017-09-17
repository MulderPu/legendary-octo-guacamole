'''
Write a Python program for Google Grocery shop to ease their cashiers to return the cash to their
customers.
'''
import sys
import locale

locale.setlocale(locale.LC_ALL, '')

def convertToUSD(number):
    number = locale.currency(number)
    return number

print('Google Grocery Shop')
print('[V]egetable selection')
print('[M]eat selection')
print('[S]eafood selection')

def calculate_vegetable (cabbage=0,french_bead=0,brinjal=0,broccoli=0):
    cabbage_price = float(2.30)
    french_per_100gram = float(1.50)
    brinjal_per_100gram = float(1.20)
    broccoli_price = float(1.80)

    result = (cabbage*cabbage_price)+(french_bead*french_per_100gram)+(brinjal*brinjal_per_100gram)+(broccoli_price*broccoli)
    return result

def calculate_meat (chicken=0, beef=0, lamp=0):
    chicken_per_100gram = float(8.50)
    beef_per_100gram = float(12.50)
    lamp_per_100gram = float(13.50)

    result = (chicken*chicken_per_100gram)+(beef*beef_per_100gram)+(lamp*lamp_per_100gram)
    return result

def calculate_seafood (fish=0, prawn=0, crab=0):
    fish_price= float(6.50)
    prawn_per_100gram = float(6.80)
    crab_per_100gram = float(5.90)

    result = (fish*fish_price)+(prawn*prawn_per_100gram)+(crab*crab_per_100gram)
    return result

def USA_curreny_coins(changes):
    dollar = int(changes)
    print('Dollar\t\t\t:', int(dollar))

    coin_left = changes-dollar
    quarter = 0
    if coin_left > 0.25:
        quarter = coin_left/0.25
        coin_left = coin_left % 0.25
    else:
        quarter = 0
    print('Quarter (25 cents)\t:', int(quarter))

    dime = 0
    if (coin_left > 0.10):
        dime = coin_left/0.10
        coin_left = coin_left % 0.10
    else:
        dime = 0
    print('Dime (10 cents)\t\t:', int(dime))

    nickle = 0
    if(coin_left > 0.05):
        nickle = coin_left/0.05
        coin_left = coin_left % 0.05
    else:
        nickle = 0
    print('Nickle (5 cents)\t:', int(nickle))

    penny = 0
    if(coin_left > 0.01):
        penny = coin_left/0.01
        coin_left = coin_left % 0.01
    print('Penny (1 cent)\t\t:',int(penny))
    
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
        broccoli = int(input('Broccoli:'))
    except ValueError:
        broccoli = 0
    total = calculate_vegetable(cabbage,french_bead,brinjal,broccoli)
    print('Total:', convertToUSD(total))
elif selection in ['m', 'M']:
    print('Meat Selection')

    try:
        chicken = int(input('Chicken:'))
    except ValueError:
        chicken = 0

    try:
        beef = int(input('Beef:'))
    except ValueError:
        beef = 0

    try:
        lamp = int(input('Lamp:'))
    except ValueError:
        lamp = 0
    
    total = calculate_meat(chicken,beef,lamp)
    print('Total:',convertToUSD(total))
elif selection in ['s', 'S']:
    print('Seafood Selection')
    
    try:
        fish = int(input('Fish:'))
    except ValueError:
        fish = 0

    try:
        prawn = int(input('Prawn:'))
    except ValueError:
        prawn = 0

    try:
        crab = int(input('Crab:'))
    except ValueError:
        crab = 0

    total = calculate_seafood(fish,prawn,crab)
    print('Total:', convertToUSD(total))

else:
    print('Wrong input. Please try again.')
    sys.exit(1)

print()
if total != float(0):
    bool = 0
    while (bool != 1):
        try:
            amount_paid = float(input('Amount Paid:'))
        except ValueError:
            amount_paid = 0
        changes = amount_paid - total

        if changes < 0:
            amount_needed = float(total-amount_paid)
            print('Your amount is not enough to pay your bill.')
            print('Please re-confirm your amount you pay.')
            print('Your total amount needed: %s'%(convertToUSD(total)))
        else:
            print('Change:', convertToUSD(changes))

            print()
            USA_curreny_coins(changes) 
            print()            
            bool=1
print('Thank you and come again.')


