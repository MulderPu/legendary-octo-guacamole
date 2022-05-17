class Solution:
    def calcFibo(self, value: int) -> list:
        a = 0
        b = 1
        c = 0
        list = []
        list.append(a)
        list.append(b)
        while c < value:
            c = a + b
            a = b
            b = c
            list.append(c)

        return list


val = 100
print(Solution().calcFibo(val))
