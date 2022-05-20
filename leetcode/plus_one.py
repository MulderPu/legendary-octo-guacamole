from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        toString = "".join(map(str,digits))
        d = int(toString) + 1
        return list(map(int,str(d)))


# digits = [4, 3, 2, 1]
digits = [9]
print(Solution().plusOne(digits))
