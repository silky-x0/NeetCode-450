# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in
# the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

left = max_ = cZero = 0

for right in range(len(nums)):

    cZero += (nums[right] == 0)

    while cZero > k:
        cZero -= (nums[left] == 0)
        left += 1

    max_ = max(max_, right - left + 1)

print(max_)     

# Same Question as LC 1493