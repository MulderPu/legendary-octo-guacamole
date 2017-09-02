#Write a Python program that asks the user to enter 2 numbers for mathematical calculation.

def sum(x,y):
    return int(x)+int(y)

def sub(x,y):
    return int(x)-int(y)

def multiply(x,y):
    return int(x)*int(y)

def divide(x,y):
    return int(x)/int(y)

print('Math Calculation')
number1 = input('Please enter 1st Number:')
number2 = input('Please enter 2nd Number:')

print(sum(number1,number2))
print(sub(number1, number2))
print(multiply(number1, number2))
print(divide(number1, number2))
