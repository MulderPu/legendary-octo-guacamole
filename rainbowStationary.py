'''
Rainbow Stationary shop is required to have a simple program for their cashier to key in customer’s
purchase.  Write a Python program to accept the inputs (purchase), calculate the cost for each item,
calculate the total of the purchase, format the answer in currency.
'''


import locale

locale.setlocale(locale.LC_ALL, '')

def convertToMYR(number):
    number = locale.currency(number).replace('$', 'MYR ')
    return number

print('Rainbow stationary')
num_pen = int(input('Pen:'))
num_pencil = int(input('Pencil:'))
num_paper = int(input('A4 Paper:'))
num_ruler = int(input('Ruler:'))
print('~**********~')

pen_price = float(1.75)
pencil_price = float(0.99)
paper_price = float(0.25)
ruler_price = float(0.50)

total_price_pen = num_pen * pen_price
total_price_pencil = num_pencil * pencil_price
total_price_paper = num_paper * paper_price
total_price_ruler = num_ruler * ruler_price
total = total_price_pen + total_price_paper + total_price_ruler + total_price_pencil

print('%i Pen(s):'%(num_pen), convertToMYR(total_price_pen))
print('%i Pencil(s):'%(num_pencil), convertToMYR(total_price_pencil))
print('%i Paper(s):'%(num_paper), convertToMYR(total_price_paper))
print('%i Ruler(s):'%(num_ruler), convertToMYR(total_price_ruler))
print('Total(MYR) purchase:', convertToMYR(total))

print('~**********~')
amount_paid = float(input('Amount Paid: MYR '))

while(amount_paid < total):
    print('not enough to pay. Please ensure you calculate correctly.')
    amount_paid=float(input('New Amount Paid: MYR '))

calculate_payment = amount_paid - total
print('Your balance:', convertToMYR(calculate_payment))

