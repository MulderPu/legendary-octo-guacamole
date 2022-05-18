from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]     #Starting with the first element
        maxSum = currentSum
        for i in range(1, len(nums)):
            print(nums[i],  currentSum + nums[i])
            currentSum = max(nums[i], currentSum + nums[i])     #Updating current sum if the current element adds more sum value
            print(currentSum)
            maxSum = max(maxSum, currentSum)                  #Updating maxSum
        return maxSum


# nums = [5, 4, -1, 7, 8]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [8,-19,5,-4,20]
print(Solution().maxSubArray(nums))
