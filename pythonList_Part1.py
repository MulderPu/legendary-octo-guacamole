'''
Create a Python List as below:
Title = ['Student ID', 'Student Name', 'Marks', 'Grade']
And now create an empty python lists: Student1[], Student2[], Student3[]
Write a Python program to accept an input for Student ID, Student Name, Marks and Grade
(separate with comma)
Write a Python program to shuffle and print the output by using a single print statement.
Note:
 “from random import shuffle” is use.
 shuffle() is use.
'''

from random import shuffle

print('Enter Student ID, Student Name, Marks and Grade (Seperate with comma)')

student1_input = input('Student 1 :')
student2_input = input('Student 2 :')
student3_input = input('Student 3 :')

student1 = student1_input.split(',')
student2 = student2_input.split(',')
student3 = student3_input.split(',')

shuffle(student1)
shuffle(student2)
shuffle(student3)

print(student1)
print(student2)
print(student3)
