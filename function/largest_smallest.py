'''
Write a Python function to find Largest and Smallest number from 3 numbers input from user.
'''
def find_largest_and_smallest(first,second,third):
    print('~Output~')
    list = [first,second,third]
    print('Largest: %s'%(max(list)))
    print('Smallest: %s'%(min(list)))

print('User Input')
first = float(input('First Number:'))
second = float(input('Second Number:'))
third = float(input('Third Number:'))
print()
find_largest_and_smallest(first,second,third)

