# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.


# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

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