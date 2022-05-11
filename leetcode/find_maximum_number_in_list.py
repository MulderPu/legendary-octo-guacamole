myList = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]


def maximumWealth(list):
    newList = []
    for item in list:
        newList.append(sum(item))
    return max(newList)


print(maximumWealth(myList))
