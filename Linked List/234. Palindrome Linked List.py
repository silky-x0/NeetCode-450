# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        st = "".join(map(str, arr))    
        return st == st[::-1]

# Alternate solution using two pointers (will add later)    