def find_uniq(arr):
    n=0
    uniq_list = set(arr)
    for i in uniq_list:
        if arr.count(i) <= 1:
            n = i
    return n

list = [1,1,1,2,3,3]
print(find_uniq(list))
