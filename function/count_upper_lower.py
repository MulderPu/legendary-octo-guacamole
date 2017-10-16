'''
Write a Python function that accepts a string (input) and calculate the number of upper case letters
and lower case letters.
'''

def count_upper_lower(str):
    upper = 0
    for i in str:
        if i.isupper():
            upper+=1
    print('Upper No: %s'%(upper))
    print('Lower No: %s'%(len(str)-upper))

str = input('Enter something with upper and lower case:')
count_upper_lower(str)
