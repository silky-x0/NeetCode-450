# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9 + 7
        i,j = 0, n-1
        count = 0
        power = [1] * n
        for k in range(1, n):
            power[k] = (power[k - 1] * 2) % MOD

        while i<=j:
            if nums[i]+nums[j] <= target:
                count=(count+2**(j-i))%MOD
                i+=1
            else:
                j-=1
        return count

sol =  Solution()
print(sol.numSubseq([3,5,6,7], 9))