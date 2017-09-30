string = input('Enter numbers *Separate by commas:')

list = string.split(',')
print('**Output**')

big_list = []
small_list = []
for i in range(len(list)):
    if int(list[i]) >= 10:
        big_list.append(list[i])
    else:
        small_list.append(list[i])

print('Values >= 10:','~'.join(big_list))
print('Values <= 10:', '~'.join(small_list))

total_big=0
total_small=0

for a in big_list:
    total_big += int(a)

for b in small_list:
    total_small += int(b)

print('Total for values >= 10: %s'%(total_big))
print('Total for value <= 10: %s'%(total_small))
