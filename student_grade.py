def check_grade (marks):
    if marks < 50:
        grade = 'fail'
    elif marks >= 50 and marks <= 65:
        grade = 'Pass'
    elif marks >= 65 and marks <=75:
        grade = 'Credit'
    elif marks > 75:
        grade = 'Distinction'

    return grade

names = input('Enter student\'s names (separated by using commas):')
marks = input('Enter student\'s marks (separated by using commas):')

studentname = names.split(',')
studentmarks = marks.split(',')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Excellent Tuition Center')

i=0
total = 0
while (i != len(studentname)):
    print('Student Name: %s\t Mark: %s\t Grade: %s'%(studentname[i], studentmarks[i],check_grade(int(studentmarks[i]))))
    total += int(studentmarks[i])
    i+=1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Total Marks: %i'%(total))
print('Average Marks: %i'%(total/len(studentmarks)))


