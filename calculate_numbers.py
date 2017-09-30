string = input('Enter numbers *separate by commas:')
print("**Output**")
lists = string.split(',')

print('List: %s'%(lists))

print('Numbers entered: %s'%(len(lists)))

total=0
for i in range(len(lists)):
    total += int(lists[i])

print('Total : %s'%(total))

print('Average: %s'%(total/len(lists)))
