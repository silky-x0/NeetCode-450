# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

s = "aab"
def palindromePart(s):
    res = []
    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start, len(s)):
            sub = s[start:end+1]
            if sub == sub[::-1]:
                backtrack(end+1, path + [sub])
    backtrack(0, [])
    return res

print(palindromePart(s))

# Notes and Explanation

# In question we're asked to provide all list of output where substring is palindrome
# in simple terms we need to do dfs until substring is palindrome and add each dfs as list 
# in result array.
'''
Goal: Return all possible partitions of string s such that every substring in the partition is a palindrome.
Key idea: Use DFS/backtracking to explore all cut positions.
Steps:
Start at index 0.
At each step, try cutting substring s[start:end+1].
If it’s a palindrome → recurse on the remainder.

Base case: if start == len(s), add current path to results.
Result: Collect each DFS path (list of substrings) into the final results array.

Palindrome check:
Simple: sub == sub[::-1] (O(k)).
Optimized: two pointers

Complexity:
Up to 2^(n-1) partitions.
Each check costs up to O(n).
Worst-case ~ O(n · 2^n).
'''