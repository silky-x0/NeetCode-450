# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

nums = [-1,0,1,2,-1,-4]
nums.sort()
res = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        sum_ = nums[i] + nums[left] + nums[right]
        if sum_ < 0:
            left+=1
        elif sum_ > 0:
            right-=1
        else:
            res.append([nums[i],nums[left],nums[right]])

            while left < right and nums[left] == nums[left + 1]:
                left+=1

            while left < right and nums[right] == nums[right - 1]:
                right-=1

            left+=1
            right-=1

print(res)

# Notes and Explanation🥰

# Idea is very simple sort the array, you may asky why? umm because we can effectively ignore duplicates numbers like question says
# give unique triplet sum to zero, so we'll fix one number and run two pointer of rest of remaining to find triplet
# if triplets sums to zero we'll append numbers and check if next number to both pointers arent same as current if yes move pointers

# for the outer loop we'll skip duplicates element using this condition if current element is equal to previous, continue and 
# 'i' of outer loop, should be greater than zero otherwise index error!

# Points to remember -
# - sort array for efficient removal of duplicates
# - fix a number find other two using two pointer
# - handle duplicates for i, left and right pointer