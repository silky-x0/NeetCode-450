# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)
        count = 0
        while i < j:
            if nums[i] == 0:
                length = 0
                while i < j and nums[i] == 0:
                    length+=1
                    i+=1
                count +=(length*(length+1))//2
            else:
                i+=1
        return count                 