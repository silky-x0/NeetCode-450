# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Time: O(n), Space: O(1)
# Two pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbols = ' ~`!@#$%^&*)(_+-=}{][|\\:;\"\'<>,.?/'
        symSet = set(symbols)
        st = s.lower()
        i, j = 0 , len(s)-1

        while i <= j:
            if st[i] in symSet:
                i += 1
                continue
            if st[j] in symSet:
                j -= 1
                continue
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1  
        return True        

# There are one liners for this problem
# s = "".join(filter(str.isalnum, s.lower()))
#        return s == s[::-1]

# I would prefer the two pointer approach as it is more readable and easier to understand.
# The one liner approach is more of a hack and less readable and that's not the point of why it is given
# Under two pointers no?!