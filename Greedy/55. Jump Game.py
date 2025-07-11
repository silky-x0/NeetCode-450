# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

 

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

nums = [2,3,1,1,4]

def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    if farthest >= len(nums) - 1:
        return True
    return False

print(canJump(nums))    

# Notes and Explanation 
# we just have to check if we can reach to end from the point where we standing
# for that we'll calculate i+nums[i], i is position and nums[i] is jump
# at each step we'll update farthest
# also check if i is greater than farthest then we'll return False. why? you might ask
# eg - [2,0,0,0,0] at index 3, farthest point i.e i + nums[i] is 2 but index is 3 and at this point we can say end is
# not reachable by any means

# at last we'll check  if farthest is greater or equal to last index of nums
