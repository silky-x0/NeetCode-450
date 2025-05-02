
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#Space Complexity: O(1)
# Time Complexity: O(n*m) where n is the number of strings and m is the length of the shortest string.

min_length = float('inf')

for s in strs:
    if len(s) < min_length:
        min_length = len(s)
        
    i = 0
while i < min_length:
    for s in strs:
        if s[i] != strs[0][i]:
            print(s[:i]) 
        i += 1
        
print( strs[0][:i])