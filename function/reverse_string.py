'''
Write a Python program to reverse a string from user input.
'''

def reverse_string(str):
    print('~Output~')
    return str[::-1]

print('User input')
str = input('What\'s your message?')
print()
result = reverse_string(str)
print('Message in reverse order: %s'%(result))
