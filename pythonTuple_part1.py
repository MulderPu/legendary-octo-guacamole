'''
Write a Python program to accept values (separate with comma) and store in tuple.
Print the values stored in tuple, sum up the values in tuple and display it. Print the maximum and
minimum value in tuple.
'''

user_input = input("Enter values (separate with comma):")

tuple = tuple(map(int, user_input.split(',')))
print('~~~~~~~~~~')
print("Values stored in tuple")
print("Tuple:",tuple)
print("~~~~~~~~~~")

print('Total:',sum(tuple))
print('Maximum',max(tuple))
print('Minimum',min(tuple))

number=int(input('Enter a number to see how many times it has appeared inside the tuple:'))
count = tuple.count(number)
if(count==0):
    print('%i appeared %i time in tuple list.'%(number,count))
else:
    print('%i appeared %i times in tuple list.'%(number, count))
