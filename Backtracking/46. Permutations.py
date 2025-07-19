# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def permutations(nums):
    res = []
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for num in nums:
            if num in path:
                continue
            path.append(num)                            # making choice
            backtrack(path)                             # DFS
            path.pop()                                  # undoing choice we made
    backtrack([])
    return res 

print(permutations([1,2,3]))

# Notes and Explanation

# A classical count based backtracking problem, we're given array as input we have to return
# All permutation to exist that will be array.length factorial, say nums = [1,2,3] permutation = 3! = 6
# base case is easy to remember like we are returning permutation means in how many ways we can fill
# array of length n, so base will be if length of path is equal to length of input array
# and as usual we'll do DFS, but one thing we need to remember that in permutation you cannot select same 
# number twice so we'll have to excplicitly check if path doesnt already have num we tryin to add
# if exist we'll skip that number.

# Points to remember
# - Base case path.length == inputArray.length
# - Check for duplicates