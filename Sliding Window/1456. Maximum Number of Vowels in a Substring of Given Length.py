# Given a string s and an integer k, return the maximum number of vowel letters in
# any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 
# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

s = "abciiidef"
k = 3

vowels = set('aeiou')
vowel_count = 0
max_vowels = 0
l = 0

for r in range(len(s)):
    if s[r] in vowels:
        vowel_count += 1

    if r - l + 1 > k:
        if s[l] in vowels:
            vowel_count -= 1
        l += 1

    max_vowels = max(max_vowels, vowel_count)

print(max_vowels)

# Notes and Explanation:
# - We use a sliding window approach to maintain the current substring of length k.
# - We expand the right end of the window by iterating through the string.
# - If the window exceeds length k, we shrink it from the left.
# - We keep track of the number of vowels in the current window and update the maximum count found.

# TC: O(n), where n is the length of the string s, SC: O(1) since we are using a fixed set of vowels.
