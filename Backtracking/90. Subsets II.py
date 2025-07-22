# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


def subsets2(nums):
    res = []
    nums.sort()
    def backtrack(start, path):
        res.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(i + 1, path + [nums[i]])
    backtrack(0,[])
    return res


print(subsets2([1,2,2]))
    

# Notes and Explanation

# same as subsets but only problem is we are given duplicates element in input array
# and is expected that we don't return duplicates subsets, to tackle this 
# Simply while building subsets we'll check if this element is not used before or is duplicate of some
# to handle this we have to sort the array.

# Intuition :- 
# to avoid duplicates maybe somehow we can check if cuurent number is taken before.

# Key points :-
# - sort the array
# - avoid duplicates