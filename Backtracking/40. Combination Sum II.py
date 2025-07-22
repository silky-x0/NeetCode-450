# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations 
# in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [[1,1,6],[1,2,5],[1,7],[2,6]]

candidates = [10,1,2,7,6,1,5]
target = 8

def combiSum2(candidates, target):
    candidates.sort()
    res = []
    def backtrack(idx, path, sum_):
        if sum_ == target:
            res.append(path[:])
            return

        if sum_ > target:
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            backtrack(i+1, path + [candidates[i]], sum_+candidates[i])

    backtrack(0, [], 0)
    return res
    
print(combiSum2(candidates, target))

# Notes and Explanation

# Same as combination sum + sorting for skipping duplicates in our resultant set, check subsets 2 for reference