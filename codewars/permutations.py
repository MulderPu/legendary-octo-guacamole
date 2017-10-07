import itertools

def permutations(string):
    data = list(string)
    permutations_list = list(itertools.permutations(data))
    new_list = []
    for i in permutations_list:
        if not i in new_list:
            new_list.append(i)
    result = []
    for j in new_list:
        str = ''.join(j)
        result.append(str)
    
    return result
string = "aabb"
print(permutations(string))
