#Using dictionary data structure as hash table
#Time complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hMap = {}
        for i,num in enumerate(nums):
            if num in hMap:
                return True
            else:
                hMap[num] = i
        return False               
        



#Using set data structure
#Time complexity: O(n)

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         visit = set(nums)
#         if len(visit) != len(nums):
#             return True
#         else:
#             return False      

# Notes 
# I was wondering which could be the optimal method to solve 
# is it using extra space or without space.....well the answer boils down to the input Sized
# of the problem like for this problem we have:
#      1 <= nums.length <= 10^5 and 10^9 <= nums[i] <= 10^9

# n is large enough that nlogn factor matters
# O(n) = about 100,000 operations
# O(nlogn) = about 100,000 times log(base 2)(100,000) equals to 1.7 million operations
# so O(n) is better

# Things to keep in mind, choose O(n) time, O(n) spcae when
# 1. time is bottleneck
# 2. n is large enough that nlogn is noticeablyslower
# 3. extra memory is acceptable

# Choose O(nlogn) time, O(1) space when
# 1. memory is limited (embedded systems, large datasets)
# 2. the inout is hue and alocating O(n) extra memory is impactical
# 3. interviewer explicityl tells you so

# In  Interviews:
# A good order is:

# Present the simplest correct solution.
# Improve the time complexity if possible.
# Discuss the space-time tradeoff.

# For example:
# "We can solve it in O(n) time using a hash map, which requires O(n) extra space.
# If constant space is preferred, we can sort the array in-place and solve it in O(n log n) time."