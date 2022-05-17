class Solution:
    def isPrime(self, value: int) -> bool:
        if value <= 2:
            return False
        if value % 10 != 0:
            return True
        return False


val = 3
print(Solution().isPrime(val))
