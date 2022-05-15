from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for item in nums:
            # check not val, then put item back in
            if item != val:
                nums[i] = item
                i += 1
        return i


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution().removeElement(nums, val))
