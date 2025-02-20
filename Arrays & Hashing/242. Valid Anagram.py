#This solution uses sorted() in built function to to arrange numbers or letter with
#respect to its corresponding ASCII character

#Time Complexity is O(n) for sorting.
#Space Complexity is O(1) since no extra space is used.

#There are other ways to do like split nd join or counting each letter but that
#would be total bs and nonsensical ig.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False