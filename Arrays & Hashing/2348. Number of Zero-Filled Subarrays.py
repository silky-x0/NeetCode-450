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


# Notes and Explanation
# Since we need to count the number of sub arrays we can do this problem using simple ye subtle method
# initialise i = 0 and j = len(nums) we'll start moving from i, towards j if we encounter nums[i] = 0
# we'll start the count of zeros in subarrays because we'll be using mathematical formula to count sum of numbers 
# upto n, why? its because we need to find all subarrays including single element [0] say we have [0,0] this
# number of zeros is 2, using formula sum or count = (2*(2+1)) // 2 which gives 3 means total subarray is
# [0], [0], [0,0] we'll be doing same for when we encounter nums[i] = 0 and i < j until nums[i] is 0 (i++ each step)
# if not we'll just increase i to move forward and return count.