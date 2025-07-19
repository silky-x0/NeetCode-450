# Given an array of distinct integers candidates and a target integer target, return a list of all unique
# combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different. The test cases are generated such that 
# the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

candidates = [2,3,6,7]
target = 7

def CombinationSum(candidates, target):
    res = []

    def backtrack(idx, path, sum_):
        if sum_ == target:
            res.append(path[:])
            return
        
        if sum_ > target or idx == len(candidates):
            return
        
        num = candidates[idx]
        backtrack(idx, path + [num], sum_ + num)
        backtrack(idx+1, path, sum_)

    backtrack(0,[],0)
    return res

print(CombinationSum(candidates, target))

# Notes and Explanation

# In this problem we are given a set of candidates (no duplicates) and a target.
# We need to find all **unique combinations** of candidates where the chosen numbers sum to the target.
# Each candidate can be chosen **unlimited number of times**.

# This problem is similar to the classic Subset Sum / Power Set generation problem, but with a twist:
# ➤ In the Power Set problem, we cannot reuse the same element multiple times.
# ➤ If we allowed repetition there, we could generate **infinite subsets** — so restrictions are essential.

# In this problem, repetition **is allowed**, but to avoid generating duplicate permutations (e.g., [2,2,3] and [3,2,2]),
# we must **always progress forward in the array** — either reuse the current index or move to the next one.

# So we use backtracking with the following base cases:
# 1. If the current sum == target → valid combination → append to result.
# 2. If the current sum > target → prune path (backtrack).
# 3. If index reaches the end of the array → stop.

# At each recursive call, we make two choices:
# - Include the current number → backtrack with same index (since repetition is allowed).
# - Skip the current number → backtrack with next index.

# I gotta revise this later again!
