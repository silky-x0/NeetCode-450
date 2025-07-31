# Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of
# one integer is that integer. A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: arr = [0]
# Output: 1
# Explanation: There is only one possible result: 0.

# Example 2:
# Input: arr = [1,1,2]
# Output: 3
# Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
res = set()
prev = set()
arr = [1,1,2]

for num in arr:
    curr = {num}
    for x in prev:
        curr.add(x | num)
    res.update(curr)
    prev = curr
print(len(res))

# Notes And Exxplanation

# Our Approach is to use a set to keep track of the distinct bitwise ORs of all subarrays.
# We iterate through each element in the array, and for each element, we create a new set `curr` that starts with the current element.
# We then iterate through the previous set of distinct ORs (`prev`) and compute the bitwise OR of each element in `prev` with the current element.
# We add these results to `curr`, and finally, we update our result set `res` with the values in `curr`.
# After processing all elements, the size of `res` gives us the count of distinct bitwise ORs of all non-empty subarrays.