max_num = 100

i=1
even=0
odd=0
while (i!=max_num):
    if(i % 2 == 0):
        even += i
    else:
        odd += i
    i += 1

print('Total for even numbers: %s'%(even))
print('Total for odd numbers: %s'%(odd))
