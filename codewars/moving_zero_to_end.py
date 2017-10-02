def move_zeros(x):
    for _ in range(len(x)-1):
        for index in range(len(x)-1):
            if x[index]==0:
                x[index+1],x[index]=x[index],x[index+1]
    return array

array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0]
print(move_zeros(array))
