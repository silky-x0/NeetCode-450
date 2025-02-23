# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# time complexity: O(n)
# space complexity: O(n)

def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                newStr.append(word1[i])  
            if i < len(word2):
                newStr.append(word2[i])  
        return ''.join(newStr)

# Approach 3: Two Pointers

# Code is self-explanatory ig.

# I found below code snippet from the Solution section of the problem.
# It is a very neat and clean code, thought if sharing it here.

   def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                res += word1[i]
            if i < len2:
                res += word2[i]
        
        return res

