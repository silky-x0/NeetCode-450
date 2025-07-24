# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string 
# "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

s = "ceabaacb"   # O/P -> 2

fmap = {}
for char in s:
    fmap[char] = fmap.get(char, 0) + 1

used, deletions =  set(), 0

for f in fmap.values():
    while f > 0 and f in used:
        f-=1
        deletions+=1
    used.add(f)

print(deletions)     

# Notes and Explanation

# So, questions says we need to find max count of deletions after which each char's frequency
# Becomes unique. we can use hashmap for frequency and a set to check if this frequency exist for any
# other character or not if yes we'll keep decreasing it until it becomes unique or it becomes zero
# also counting number of deletions each time, easy peasy ig!