import sys

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

print('Excellent Tuition Center')
student_name = input('Student Name:')

max_subject =5
try:
    no_of_subject = int(input('Number of subjects (3/5):'))
    if no_of_subject > 5:
        no_of_subject=5

    x=1
    lists = []
    mark_lists = []
    while (x <= no_of_subject):
        list = []
        subject = ''
        mark = ''
        subject = input('Subject %i:'%(x))
        mark = float(input('Marks:'))
        grades = check_grade(mark)
        list.append(subject)
        list.append(mark)
        list.append(grades)
        mark_lists.append(mark)
        lists.append(list)
        x+=1

    print('~~~~~~~~~~~~~~~')
    print('Student name: %s'%(student_name))

    list_size = len(lists)
    y=0
    z=1
    while list_size != 0:
        print('Subject %i: %s'%(z,lists[y][0]),'Mark: %0.1f'%(lists[y][1]),'Grade: %s'%(lists[y][2]))
        y+=1
        z+=1
        list_size -=1
    print('~~~~~~~~~~~~~~~')
    highest = max(mark_lists)
    high_index = mark_lists.index(highest)
    print('Highest Marks: %0.1f'%(lists[high_index][1]), 'Subject: %s'%(lists[high_index][0]))
    lowest = min(mark_lists)
    low_index = mark_lists.index(lowest)
    print('Lowest Marks: %0.1f'%(lists[low_index][1]), 'Subject: %s'%(lists[low_index][0]))
    print('~~~~~~~~~~~~~~~')

    total = float(sum(mark_lists))
    print('Total Marks: %0.1f'%(total))
    average = total / len(mark_lists)
    print('Average Marks: %0.2f'%(average))
    print('Overall Marks: %s'%(check_grade(average)))
except ValueError:
    print('Please enter number only.')
    sys.exit(1)
