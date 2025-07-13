# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
# sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

target = 7
nums = [2,3,1,2,4,3]

def minSizeSubarr(nums, target):
    if target > sum(nums):
        return 0
    
    left, minSize, window = 0, float('inf'), 0
    for right in range(len(nums)):
        window+=nums[right]

        while window >= target:
            minSize = min(minSize, (right-left)+1)
            window-=nums[left]
            left+=1
    return minSize

print(minSizeSubarr(nums, target))

# Notes and Explanantion

# lets first revise question it is said that we have to find minimum length of subarray of sum greater than or equal to target
# Now like for question where it is asked something like subarray with some condition most of the question can be solved using 
# sliding window technique, here we maintain two pointers to increase our window(virtually) size here we keep increasing
# our window until some condition is triggered then we'll decrease from left until that condition is nullified,
# here we have to find subarray with sum equal or greater than target, our main idea is to find all subarray of sum 
# greater or equal to target and keep track of minimum length, thats it nothing more!