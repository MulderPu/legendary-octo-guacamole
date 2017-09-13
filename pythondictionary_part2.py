'''
Create a python dictionary as below:
Student_List = 1000145:85.5, 1000159:77, 1000258:61.5, 1000112:55.8
Calculate and display the total and average of the values.
Write a python program to update the dictionary by adding 2 more information:
1000147:61.5 and 1000588:55
And now re‐calculate and display the total and average of the values.
Note: “update” will be used.
'''

dict= {'1000145': 85.5, '1000112': 77, '1000258': 61.5, '1000159':55.8 }
print("Original List:",dict)
total = sum(dict.values())
print("Total:",total)
average = total / len(dict)
print("Average:",average)

dict['1000147'] = 61.5
dict['1000588'] = 55

print()
print("After Update:",dict)
new_total = sum(dict.values())
print("Total:",new_total)
new_average = new_total / len(dict)
print("Average:",new_average)



