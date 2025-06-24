# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

s = "leetcode"
wordDict = ["leet","code"]
n = len(s)
memo = [False]*(n+1)
memo[0] = True
for i in range(1,n+1):
    for j in range(i):
        if memo[j] and s[j:i] in wordDict:
            memo[i] = True
            break
print(memo[n])        