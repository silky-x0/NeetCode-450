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