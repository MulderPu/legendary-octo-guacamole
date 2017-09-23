'''
Write a Python program to check the validity of a password (input from users).
Validation :





At least 1 letter between [a‐z] and 1 letter between [A‐Z].
At least 1 number between [0‐9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''

import re

def validate_password():
    special_char = '@#$'
    while True:
        password = input("Enter a password: ")
        if len(password) < 6:
            print("Make sure your password is at least 6 letters.")
        elif len(password) > 16:
            print("Make sure your password is not more than 16 letters.")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it.")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it.")
        elif re.search('[a-z]',password) is None: 
            print("Make sure your password has a letter in it.")
        elif re.search ('[@#$]', password) is None:
            print("Make sure your password has a special character [@#$]")
        else:
            print("Your password seems fine")
            break

validate_password()
