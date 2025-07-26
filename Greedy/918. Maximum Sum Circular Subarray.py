# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element
# of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray 
# nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Example 2:
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Example 3:
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

nums = [5,-3,5]

def maxSubArrayCircular(nums):
    maxLocal, minLocal = nums[0], nums[0]
    maxGlobal, minGlobal = nums[0], nums[0]

    for num in nums[1:]:

        minLocal = min(num, minLocal+num)
        minGlobal = min(minGlobal, minLocal)

        maxLocal = max(num, maxLocal+num)
        maxGlobal = max(maxGlobal, maxLocal)

    total = sum(nums)
    if maxGlobal < 0:
        return maxGlobal
    
    return max(maxGlobal, total - minGlobal)

print(maxSubArrayCircular(nums))


# Notes and Explanation

# First of all problem description is too technical (for me at least), in simple terms
# we are given array i.e circular means we can go to first from end and vice versa(means end and front are connected)
# and we need to find maxs sum of subarray present, we'll be using kadane's Algo because brute - force will result in
# TC of n^2 which we do not want for larger input like in problem 1 <= Array.length <= 3 * 104 
# Honestly i didnt have idea what to do i mean i have but that was wrong, orginally i thought of to flatten array
# or maybe use padding first and last element and vice versa but logic wasnt correct, I looked thru discussion section then i got hint

# Approach and Intuition

# Main idea is to find max Subarray and min Subarray using kadane's Algo, why? because if all numbers are negative we can return
# maxGlobal sum, and if not we'll return max of maxglobal and total sum - minGlobal, you may ask why.. because say we are given array
# [2,-4,-3,1], toal sum = -4, minGlobal = -7, maxGlobal = 2.... so if we remove our minimum array from total we can get maxSum
# including first and last, say we remove [-4,-3] we left with [2,1] now we can return if computed maxGlobal is greater or
# values including first and last, and this works!
# like if you want to test this umm explanation like your not clear with it try dry running above code on testcases
# nums = [2,-4,-3,1]
# nums = [5,-3,5]
# nums = [2,-4,-3,-1]
# nums = [-2,-4,-3,-1]
