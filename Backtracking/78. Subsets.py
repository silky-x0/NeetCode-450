# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


nums = [1,2,3]

def subsets(nums):
    res = []
    def backtrack(idx, path):
        if idx == len(nums):
            res.append(path)
            return 
        backtrack(idx + 1, path + [nums[idx]])
        backtrack(idx + 1, path)

    backtrack(0, [])
    return res

print(subsets(nums))

# Notes and Explanation

# All this(backtracking) is part of big plan Recursion, so basic of recursion is making descision based of two choices 
# either do this or skip this, in this question for each element we're selecting if it has to be added in path(current res) or not
# by recursively exploring both choices for every element in the input array.
# and we'll be going until index == length of nums and we'll append that result in our result set.
# if its confusing try making recusrion tree for this problem to visualise!