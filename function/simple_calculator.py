'''
Write a Python “function” for the following output.

Conditions:
There are 5 selections:
[A]ddition, [S]ubtraction, [M]ultiplication, [D]ivision, and [Q]uit to stop the process.
The selection will accept uppercase or lowercase as input (no case‐sensitive issue).
Note:Use Python function to store the formulas and accept user input (for first number and second
number only).
'''
import sys

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def print_choice():
    print('Mathematical Calculator')
    print()
    print('[A]ddition')
    print('[S]ubstraction')
    print('[M]ultiplication')
    print('[D]ivision')
    print('[Q]uit')

flag = 1
while (flag):
    print_choice()
    selection = input('Selection:')
    if selection in ['a','A']:
        a = int(input('Enter first number:'))
        b = int(input('Enter second number:'))
        print('Addition answer:',sum(a,b))
        print()
        print('--------------------------')
    elif selection in ['s', 'S']:
        a = int(input('Enter first number:'))
        b = int(input('Enter second number:'))
        print('Substraction answer:',sub(a,b))
        print()
        print('--------------------------')
    elif selection in ['m','M']:
        a = int(input('Enter first number:'))
        b = int(input('Enter second number:'))
        print('Multiplication answer:',mul(a,b))
        print()
        print('--------------------------')
    elif selection in ['d','D']:
        a = int(input('Enter first number:'))
        b = int(input('Enter second number:'))
        print('Division answer:',div(a,b))
        print()
        print('--------------------------')
    elif selection in ['q','Q']:
        print('Thank You, please come again.')
        flag=0
    else:
        sys.exit('Wrong Input.')
