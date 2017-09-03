'''
Write a Python program to accept 2 “string” numbers for calculation.  Note: convert string number
to an Integer number before perform the calculation.
'''


string1 = input('Enter a first string integer:')
string2 = input('Enter a second string integer:')

num1 = int(string1)
num2 = int(string2)

print("Sum of %i + %i =" %(num1,num2), num1+num2)

