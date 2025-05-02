def LCS(s1: str, s2: str) -> int:
    dp = {}  # Memoization dictionary
    
    def dfs(i: int, j: int) -> int:
        if i >= len(s1) or j >= len(s2):
            return 0
        
        if (i, j) in dp:
            return dp[(i, j)]
        
        if s1[i] == s2[j]:
            dp[(i, j)] = 1 + dfs(i + 1, j + 1)
        else:
            dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            
        return dp[(i, j)]
    
    return dfs(0, 0)

# Test the function
s1 = "abccbca"
s2 = "abecb"
print(LCS(s1, s2))  # Should print 4 (longest common subsequence is "abcb")