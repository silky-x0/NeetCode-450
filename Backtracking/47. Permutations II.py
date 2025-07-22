# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:[[1,1,2], [1,2,1], [2,1,1]]

def permu2(nums):
    n = len(nums)
    nums.sort()
    used = [False]*n
    res = []

    def backtrack(path):
        if len(path) == n:
            res.append(path[:])
            return
        
        for i in range(n):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                continue
            used[i] = True
            backtrack(path + [nums[i]])
            used[i] = False
    backtrack([])
    return res

print(permu2([1,1,2]))

# Notes and Explanation
# This is a variation of the permutation problem where we have to handle duplicates.
# The key is to sort the input array and use a boolean array to track which elements have been used.
# We also need to ensure that we skip over duplicates by checking if the current element is the
# same as the previous one and if the previous one was used.

# Key points:
# - sort the array to handle duplicates easily
# - use a boolean array to track used elements
# - skip duplicates by checking the previous element
# - base case is when the path length equals the input array length
# - return the result when the base case is met

# Have to revise this later