'''
Write a Python function to display Odd numbers and Even numbers from user input (store in list).
'''

def odd_and_even(str):
    print()
    print('~Output~')
    list = str.split(',')

    even = []
    odd = []
    for i in list:
        if(int(i) % 2 == 0):
            even.append(i)
        else:
            odd.append(i)

    print('Even numbers:', '~'.join(even))
    print('Odd numbers:', '~'.join(odd))
    


str = input('Enter numbers *separate by commas:')
odd_and_even(str)
