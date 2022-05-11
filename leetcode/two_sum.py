num = [2, 5, 5, 11]
target = 10


def two_sum(number_list, target):
    length = len(number_list)
    n1 = 0
    n2 = 0
    ans = []
    for i in range(0, length):
        n1 = number_list[i]
        for j in range(i + 1, length):
            n2 = number_list[j]
            if (n1 + n2) == target:
                ans.append(i)
                ans.append(j)
                return ans


print(two_sum(num, target))
