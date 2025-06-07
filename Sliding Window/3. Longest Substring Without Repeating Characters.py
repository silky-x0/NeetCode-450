# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

def longestSubstringWoutReChar(s):
    charSet = set()                      #O(1)
    maxLen = 0                           #O(1)     
    i = 0                                #O(1)
    for j in range(len(s)):              #O(n)
        while s[j] in charSet:           #O(1) hash lookup
            charSet.remove(s[i])         #O(1)
            i+=1
        charSet.add(s[j])
        maxLen = max(maxLen, j - i + 1)

    return maxLen

print(longestSubstringWoutReChar("pwwkew"))

#Before I wrote a terrible solution! there i used hashtable when instead of increasing window size and decreasing i was just jumping i to j if element was present in map and j to j + 1

#But well this fine, Time complexity is O(n)