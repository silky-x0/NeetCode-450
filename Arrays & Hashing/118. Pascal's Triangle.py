
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Space Complexity: O(n^2) where n is the number of rows in the triangle.
# Time Complexity: O(n^2) where n is the number of rows in the triangle.

triangle = [[1]]
numRows = 5
for i in range(numRows-1):
    temp = [0] + triangle[-1] + [0]
    row = []
    for j in range(len(triangle[-1])+1):
        row.append(temp[j] + temp[j+1])
    triangle.append(row)

print(triangle)    
