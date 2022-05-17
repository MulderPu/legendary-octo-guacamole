from typing import List


class Solution:
    # You must write an algorithm with O(log n) runtime complexity.

    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target > nums[0]:
            return 1

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif i+1 < len(nums) and target < nums[i+1]:
                if target < nums[i]:
                    return i
                return i + 1
            elif i+1 == len(nums) and len(nums) > 1:
                return len(nums)
            else:
                continue
        return 0


# nums = [1, 3, 5, 6]
# target = 5
# nums = [1, 3, 5, 6]
# target = 7
nums = [1]
target = 2
print(Solution().searchInsert(nums, target))
