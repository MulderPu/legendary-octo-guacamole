'''
Write a Python program to create an empty set, name as color_set, now add the following items into
color_set. (Note: add is use.)
color_set: white, pink, black
And now, using input function to accept user input then later update the color_set. (Note: update is
use.)
Input: red, purple, green, blue, purple, orange, navy blue, apple green
Last, accept an input to remove the color from the set. (Note: discard is use.)
'''
color_set = set()
color_set.add('white')
color_set.add('pink')
color_set.add('black')
print('Current List:',color_set)
string = input('Enter some color:')
list = string.split(',')

new_set = set()
for item in list:
    new_set.add(item)
color_set.update(new_set)
print('New List:',color_set)

item_to_delete = input('Enter item that you want to delete:')
color_set.discard(item_to_delete)
print('Result:',color_set)
