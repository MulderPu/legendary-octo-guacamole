'''
Write a Python program to accept an input for 12 months (separate with comma) and now accept
another input for months and find the difference from each other.
Note:
 List and set will be used.
 months.split(‘,’) is use.
'''

months_input = input('Enter 12 months (seperate with comma):')

months_list = months_input.split(',')

print(months_list)

remove_input = input("Enter a month to be removed from the list:")

print('%s will be removed from the list'% [remove_input])

months_list.remove(remove_input)
print('New List:', months_list)
