# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.strip()
        count = 0
        if " " in str:
            for i in range(len(str)-1,-1,-1):
                count+=1
                if str[i] == " ":
                    return count-1
        return len(str)


# Alternate solution(one liner)     

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
    
# Time complexity: O(n)
# Space complexity: O(n)


# Alternate solution for constant space complexity(I found this on web thought of sharing it here)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Count characters until next space
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length