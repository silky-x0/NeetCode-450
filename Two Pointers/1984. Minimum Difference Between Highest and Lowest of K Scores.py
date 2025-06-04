# Example 1:
# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.

# Example 2:
# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.

#In-short maxSubarray of size k, return minimum difference

def minimumDifference(nums: list[int], k: int) -> int:
        if k == 1:
            return 0
        if len(nums) == k:
            return max(nums) - min(nums)                        #O(n)
        nums.sort()                                             #O(nlogn)
        i,j = 0,k-1
        minDiff = float("+inf")
        while j < len(nums):                                    #O(n)
            minLocal = max(nums[i:j+1]) - min(nums[i:j+1])      #O(n)
            minDiff = min(minLocal, minDiff)                    #O(1)
            i+=1
            j+=1

        return minDiff

nums = [9,4,1,7]
k = 2
print(minimumDifference(nums, k))

#Time Complexity:- O(n) + O(nlogn) + O(n) + O(n) + O(1) = O(nlogn)