#This solution uses sorted() in built function to to arrange numbers or letter with
#respect to its corresponding ASCII character

#Time Complexity is O(n) for sorting.
#Space Complexity is O(1) since no extra space is used.

#There are other ways to do like split nd join or counting each letter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


# new approach to do this: (better method)

def isAna(s, t):
    if len(s) == len(t):
        return False

    ch = {}

    for i in range(len(s)):
        ch[s[i]] = ch.get(s[i], 0) + 1 
        ch[t[i]] = ch.get(t[i], 0) - 1

    for val in ch.values():  
        if val != 0:
            return False

    return True


# Code is self explanatory because we're incrementing and decrementing at same time
# and if character counts are same then the values would be 0.
                
                        