def count_smiley(arr):
    smile=0
    for i in arr:
        print(i)
        if (')' in i and ':' in i) or (';' in i and ')' in i):
            smile +=1
        elif ('D' in i and ':' in i) or (';' in i and 'D' in i)  :
            smile +=1
    return smile

list = [':)', ';(', ';}', ':-D']
print(count_smiley(list))
