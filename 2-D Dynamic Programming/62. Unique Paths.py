# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
# or right at any point in time. Given the two integers m and n, return the number of possible unique 
# paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

m = 3
n = 2

dp = [[1]*n for _ in range(m)]

for i in range(1,m):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(dp[-1][-1])


# Notes and Explanation

# Question says we/robot are at starting of 2D matrix i.e in position 0,0 and
# in how many ways we can reach end position i.e i-1, j-1 with movement right and down
# we'll use 2D array and for each position we can count in how many ways we can reach there
# so instead of computing path manuall we can just check dp[i-1][j] and dp[i][j-1] and sum them
# to put into dp[i][j] why? u might ask, so its because question says we can move only right
# and down, so dp[i-1][j] check upper cell like we can can reach to a position by moving
# down if we came from upper cell right, same for left cell i.e dp[i][j-1]
# and for the starters we'll assign 1st row and column with 1, why? because
# there are exactly one path you can reach in certain row(dp[i][0]) or column(dp[0][j])
# btw, above we initiliased every cell with 1 and re-evaluating path to reach skipping
# left and upper edge, and return last cell value(end point)

# Optimization
# we can optimise space little bit right now its O(m*n) we can make it O(n), using 1D array
# we'll need current row and previous row value and that can be done with array

'''
m, n = 3, 2
dp = [1]*n

for _ in range(1, m):
    for j in range(1, n):
        dp[j]= dp[j] + dp[j-1]

print(dp[-1])    

'''