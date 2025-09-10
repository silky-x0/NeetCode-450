# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
# Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

nums = [0,1,1,1,0,1,1,0,1]

left = cZero = max_ = 0

for right in range(len(nums)):

    cZero += (nums[right] == 0)

    while cZero > 1:
        cZero -= (nums[left] == 0)
        left+=1
    max_ = max(max_, right - left + 1)

print(max_ - 1)

# Notes and Explanation
# Here Our problem is simple we need to calculate max length of subarray with at at most 1 0's in it and because
# we need to delete it as question says, so simple we using sliding window technique and keep count of zero
# if at any point count of zero exceeds 1 we can begin shrinking our window from left until count of zero
# goes back to 1(ofc at each step we'll shrink from left at and if nums[left] is 0 or not if yes decrease 
# count of zero increase left else increase left) simple and at each point we calculate max lenght of our window
# since we need to return only count of 1's without 0 or simply as question says we need to delete one element in array
# so we'll print/return max_ - 1, this handles even if our array doesnt containes zero since we still need to delete one
# element.

# Similar question - LC 1004 Max Consecutive One's 3, and there we can flip/delete only k.