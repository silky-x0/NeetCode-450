# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i+=1
        if i == len(s):        
            return True
        return False


#time complexity: O(n)
# space complexity: O(1)

# Approach:
# 1. Initialize a pointer i to 0.
# 2. Iterate through the string t.
# 3. If the character at index i of s is equal to the character at index j of t, increment i.
# 4. If i is equal to the length of s, return True.
# 5. If the loop completes, and if statement is not true--> return False.
# 
# Technique: Two-pointer
# Where we used two pointers to iterate through the strings s and t simultaneously.   