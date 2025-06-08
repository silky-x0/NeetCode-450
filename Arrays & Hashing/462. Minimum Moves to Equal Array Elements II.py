# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

# In this question we have to do with median!! not the minimum or maximum value because on
# LC-453 we can only increment or decrement but here we can do both operation.

def minMoves2(self, nums: list[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        nums.sort()                      #O(nlogn) time complexity
        median = nums[len(nums)//2]
        totalMoves = 0
        for num in nums:
            totalMoves+=abs(num-median)
        return totalMoves

# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(1) since we are using constant space