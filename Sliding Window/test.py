# Input:

#     ADOBECODEBANC
#     ABC

# Output:

#     BANC

# Explanation:
#     The minimum window containing 'A', 'B', and 'C' is "BANC".
from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"
tmap = Counter(t)

fmap = {}
left = 0
minSizeArr = []
minSize = -1
for right in range(len(s)):
    char = s[right]
    fmap[char] = fmap.get(char, 0) + 1

    if tmap[char] < fmap[char]:
        fmap[char]-=1
        left+=1
    minSize = min(minSize, right-left+1)    
print(minSize)    