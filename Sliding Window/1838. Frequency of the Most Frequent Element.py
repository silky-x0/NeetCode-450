# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums
# and increment the element at that index by 1
# Return the maximum possible frequency of an element after performing at most k operations.

# Example 1:
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.

nums = [1,2,4]
k = 5

nums.sort()
sum_ = l = 0
max_ = -1

for r in range(len(nums)):
    sum_ += nums[r]
    cSize = r - l + 1
    need = nums[r] * cSize - sum_

    while need > k:
        sum_ -= nums[l]
        l+=1
        need = nums[r] * cSize - sum_

    max_ = max(cSize, max_)

print(max_)

# Notes and Explanation
