string = input('Enter numbers *Separate by commas:')

list = string.split(',')
print('**Output**')

big_list = []
small_list = []
even_list= []
odd_list = []
total=0
for i in list:
    if int(i) >= 10:
        big_list.append(i)
    else:
        small_list.append(i)

    if int(i) % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
    total += int(i)

print('Values >= 10:','~'.join(big_list))
print('Values <= 10:', '~'.join(small_list))

total_big=0
total_small=0

for a in big_list:
    total_big += int(a)

for b in small_list:
    total_small += int(b)

print('Total for values >= 10: %s'%(total_big))
print('Total for values <= 10: %s'%(total_small))
print('Numbers of even values: %s'%(len(even_list)))
print('Numbers of odd values: %s'%(len(odd_list)))
print('Even values :', '~'.join(even_list))
print('Odd values :', '~'.join(odd_list))
print('Total: %s'%(total))
