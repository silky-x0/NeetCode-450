# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

perimeter = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            if i == 0 or grid[i-1][j] == 0:
                perimeter+=1
            if i == len(grid) - 1 or grid[i+1][j] == 0:
                perimeter+=1
            if j == 0 or grid[i][j-1] == 0:
                perimeter+=1
            if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                perimeter+=1

print(perimeter)

#Our main idea is to add perimeter when grid above, below, left, right is 0 or out of bounds-  for current grid
#in simple way we are adding perimeter for each side when any of side isn't touching to other land/islands

#i know, i'll also do this with dfs/bfs later!