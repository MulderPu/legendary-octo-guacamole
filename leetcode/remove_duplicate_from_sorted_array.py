from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for item in nums:
            if i == 0:
                nums[i] = item
                i += 1
            elif item > nums[i-1]:  # check previous number
                nums[i] = item
                i += 1
        return i


nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
