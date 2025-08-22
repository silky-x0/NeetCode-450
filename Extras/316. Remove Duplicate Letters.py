# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.


# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"
from collections import Counter
s = "cbacdcbc"

freq = Counter(s)
seen = set()
stack = []
for c in s:
    freq[c]-=1
    if c in seen:
        continue
    while stack and stack[-1] > c and freq[stack[-1]]>0:
        seen.remove(stack.pop())
    stack.append(c)
    seen.add(c)
print("".join(stack))

# Notes and Explanation (will add later)
# Core idea is to use stack and greedy approach
# we will use frequency map to track how many times a char has appeared
# we will use seen set to track which char has already been added to stack
# we will iterate over each char in string 
# we will decrease its frequency in fmap
# if char is already in seen we will skip it
# else we will check if stack is not empty and top of stack is lexicographically greater
# than current char and frequency of top of stack char is greater than 0
# freq > 0 means "this character will come again later, so I can pop it now for a better lexicographic order.
# if all above condition is true we will pop the top of stack and remove it from seen
# we will repeat above step until all condition is false
# finally we will add current char to stack and seen