# You are given a 0-indexed integer array nums and an integer threshold.

# Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:

#     nums[l] % 2 == 0
#     For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
#     For all indices i in the range [l, r], nums[i] <= threshold

# Return an integer denoting the length of the longest such subarray.

# Note: A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [3,2,5,4], threshold = 5
# Output: 3
# Explanation: In this example, we can select the subarray that starts at l = 1 and ends at r = 3 => [2,5,4]. This subarray satisfies the conditions.
# Hence, the answer is the length of the subarray, 3. We can show that 3 is the maximum possible achievable length.

curr = 0
res = 0
nums = [3,2,5,4]
threshold = 5

for i in range(len(nums)):
    if nums[i] > threshold:
        curr = 0
        continue

    if curr == 0:
        if nums[i] & 1 == 0:
            curr = 1
            res = max(res, curr)
        continue

    if (nums[i] & 1) != (nums[i - 1] & 1):
        curr += 1
        res = max(res, curr)
    else:
        if nums[i] & 1 == 0:
            curr = 1
        else:
            curr = 0

print(res)

# Notes and explanation
# We simply have to find the longest even-odd alternating subarray with the first element being even
# and all elements being less than or equal to threshold. 
# Our main idea will be to start subarray at every even element and keep on adding elements
# to the subarray also simultaneously checking if the element is less than or equal to threshold
# and indeed we'll have to check for alternating pattern as questions says.ArithmeticError

# Mental run:
# say we have array of [3,2,5,4] and threshold = 5
# we'll check if first element is even and less than or equal to threshold
# if it is we'll add increase our curr(element count) by 1 and update our global max(res)
# because at every point we're choosing if we'll continue or start a new subarray
# and in next step we'll check for alternating pattern i.e even-odd-even if satisfies
# we'll increase our curr by 1 and update our global max(res)
# if it doesnt satisfies we'll check if we can start new subarray or not (checking for even)
# if even we'll reset our subarray count to 1
# if odd we'll reset our subarray count to 0

# Time complexity: O(n)
# Space complexity: O(1)
