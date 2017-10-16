'''
Write a Python function that accepts student names and marks (store in list).
Calculate the total marks and average based on the input.
'''

def student_mark(name, marks):
    print()
    print('~Output~')

    studentname = names.split(',')
    studentmarks = marks.split(',')

    i=0
    total = 0
    while (i != len(studentname)):
        print('Student Name: %s\t | Marks: %s'%(studentname[i], studentmarks[i]))
        total += int(studentmarks[i])
        i+=1
    print('Total of %s student\'s marks: %i'%(len(studentname),total))
    print('Average is: %i'%(total/len(studentmarks)))



names = input('Enter name *separate by commas:')
marks = input('Enter marks *separate by commas:')

student_mark(names, marks)
