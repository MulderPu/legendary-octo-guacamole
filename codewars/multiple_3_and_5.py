def solution(number):
    list = []
    lists = ['3','5']
    for i in range(1,12):
        for j in range(len(lists)):
            result = int(lists[j]) * i

            if(int(result) < number):
                list.append(int(result))
            else:
                break
    return sum(list)

print(solution(10))
