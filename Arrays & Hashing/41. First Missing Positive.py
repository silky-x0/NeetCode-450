# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
# nums = [1,2,0]
for i, num in enumerate(nums):
    if num <= 0:
        nums[i] = float('inf')
print(nums)
for n in nums:
    val = abs(n)
    if 1 <= val <= len(nums):
        nums[val-1] = -1 * abs(nums[val-1])
print(nums)

for i in range(len(nums)):
    if nums[i] > 0:
        print(i+1)
        break
else:
    print(len(nums)+1)

# Notes and Explanation
# For this question there can be multiple answers if we ignore constant space contraint and obviously
# without it this become easy problem, like we can do with brute force two nested loops(n^2) or by sorting(nlogn)
# or maybe using O(n) space using set or hashmap, but we have we have and are doing in constant space by 
# manipulating given array, core idea is to mark index with -ve values to keep track of element in array

# Example and walkthrough
# nums = [3,4,-1,1]
# since we know minimum +ve positive number is 1 and missing integer can can range from 1 to nums.length inclusively, why? 
# because say in above array min +ve is 1 and length is 3 so in array all number from 1 to 3 should be present to be it of length 3
# right, if not means some integer is missing say we have nums = [99,1,100] length is 3, so missing integer must lie in range 1 to 3
# if not its nums.length + 1, now we optimised a little bit out search range which in original(brtue force) was min(nums) to max(nums) incl.

# In next step we'll set negatives and zeros to -infinity, since we are only concerned about +ve integer why? we'll understand
# this in last step keep this in mind. 
# nums becomes = [3, 4, inf, 1]

# In this step we'll interate over num in nums and check if num lies in range of 1 to len(nums) [why? we discussed this earlier]
# if yes we mark its index value -ve by multiplying -1 to its index's value, eg nums = [3, 4, inf, 1], for abs(num) = 3 we'll choose index
# 3 - 1 (0 based indexing) i.e nums[2] = inf and multiply with -1, with this we've marked that 3 is present in array same for abs(num) = 4
# 4 - 1 i.e  nums[3] = 1 and multiplying with -1, next for abs(num) = abs(-inf), [this is the the reason we're using aboslute val, coz maybe any other
# number is marked in this index like here, -inf shows 3 is present in array] but since we're checking if num between 1 to len(nums) it'll
# not pick inf/-inf as of last, num = 1, 1 - 1 i.e nums[0] = 3 and multiplying -it with -1
# our array becomes, nums = [-3, 4, -inf, -1]

# last step, we'll check if any value is still positive means extra but we're not concerned for that but rather then value in that position
# we'll iterate over nums checking if nums[i] > 0 if yes means this, number and its index has not been marked, and since we checked for
# num ranging 1 to nums.length means its sure that this index will hold missing number that we'll return index + 1
# else we'll return len(nums) + 1.