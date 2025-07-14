# You are given a string s and an integer k. You can choose any character of the string and change it to any other 
# uppercase English character. You can perform this operation at most k times.Return the length of the longest substring
# containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

s = "ABAB"
k = 2

maxCount, maxLen, left, fmap = 0, 0, 0, {}

for right in range(len(s)):
    char = s[right]
    fmap[char] = fmap.get(char, 0) + 1
    maxCount = max(maxCount, fmap[char])

    if right - left + 1 - maxCount > k:
        fmap[char]-=1
        left+=1

    maxLen = max(maxLen, right - left + 1)

print(maxLen)

# Notes and Explanation

# In simple terms we have to find max length of subarray which has at most k odd element, eg say s = "ABABB" , k = 1
# one subarray is "ABA" with k = 1 odd element i.e B has length of 3 whereas 2nd subarray is "BABB" with 1 odd element A has length of 4 so we'll return 4
# so our idea is we'll not replace most dominant character in string but other than that, so we'll keep count of most frequent element(in current window)
# and max length of subarray that satisfies the condition, for that we'll use hashmap to store frequencies
# our core idea is when charcater replacement is greater than k we'll shrink the window by one, using this condn
# window - maxCount(element with most frequencies within current window) > k .... you may ask why this?
# say we have s = "AAAB" length of window is 4, max count of frequent element is 3 so 4 - 3  = 1, means we need to change one element to make the all same
# now K tells us max replacement we can do, we're checking if current window has elements which are needed to be replaced and their count is less than k.

# Here's Quick question why didint we updated maxCount when shrinking window? (think, think)

# Answer - because we only substracted our window by one and if future its sure that count will increase to current value so we did little cheating
# and sole reason is that we didnt use while loop for shrinking window like other sliding window problem because we'didnt update maxCount which 
# could cause our window to shrink by alot than we want to, so here we'll keep shrinking by one that'll do the work

# (we know with great shortcut comes small tradeoffs, but in this case, it helps us write a clean and efficient solution without breaking correctness.)