from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)

        for row in wall:
            edge_pos = 0
            for i in range(len(row) - 1):  
                edge_pos += row[i]
                edge_count[edge_pos] += 1


        return len(wall) - max(edge_count.values(),default=0)
    
#Time Complexity: O(n*m), where n is the number of rows and m is the average number of bricks in each row.

#Have to revise this Later :)