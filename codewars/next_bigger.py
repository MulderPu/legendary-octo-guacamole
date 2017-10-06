def next_bigger(n):
    list = []
    for i in str(n):
        list.append(i)
    print(list)
    try:
        i = max(i for i in range(1,len(list)) if list[i-1] < list[i])
    except ValueError:
        return -1

    try:
        j = max(j for j in range(i,len(list)) if list[j] > list[i-1])
    except ValueError:
        return -1
    
    list[j], list[i-1] = list[i-1], list[j]
    list[i:] = reversed(list[i:])
    new_num = int(''.join(list))
    if new_num == n:
        return -1
    return new_num
num = 111
print(next_bigger(num))
