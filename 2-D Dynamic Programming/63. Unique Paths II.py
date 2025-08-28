#--PROBLEM DESCRIPTION---




class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        col = len(Grid[0])
        row = len(Grid)
        
        if Grid[0][0] == 1 or Grid[row-1][col-1] == 1:
            return 0
        
        dp = [[0]*col for _ in range(row)]
        dp[0][0] = 1
        
        # First row
        for i in range(1, col):
            if Grid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
        
        # First column
        for j in range(1, row):
            if Grid[j][0] == 0:
                dp[j][0] = dp[j-1][0]
        
        # Rest of the table
        for i in range(1, row):
            for j in range(1, col):
                if Grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]


# Notes and Explanation (will add later)