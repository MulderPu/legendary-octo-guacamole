'''
Write a Python program to find the sum, average, minimum and maximum values from the items in
a dictionary.
Please store 5 students’ marks into python dictionary: 78,64,62,56,71
'''

dict = dict(stud1=78, stud2=64, stud3=62, stud4=56, stud5=71)
total = dict['stud1'] + dict['stud2'] + dict['stud3'] + dict['stud4'] + dict['stud5']
print("Total marks (among %i students):"%(len(dict)),total)

size_of_dict = len(dict)
average = total / size_of_dict
print("Average marks (among %i students)"%(size_of_dict),average)

print("Minimum marks (among %i students)"%(size_of_dict),min(dict.values()))
print("Maximum marks (among %i students)"%(size_of_dict),max(dict.values()))
