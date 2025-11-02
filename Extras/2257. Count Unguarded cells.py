class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]

        for i, j in guards:
            mat[i][j] = 1   # guard
        for i, j in walls:
            mat[i][j] = 2   # wall

        # Sweep rows (left -> right, then right -> left)
        for i in range(m):
            seen_guard = False
            for j in range(n):
                if mat[i][j] == 2:
                    seen_guard = False
                elif mat[i][j] == 1:
                    seen_guard = True
                elif seen_guard:
                    mat[i][j] = 3  # guarded

            seen_guard = False
            for j in range(n-1, -1, -1):
                if mat[i][j] == 2:
                    seen_guard = False
                elif mat[i][j] == 1:
                    seen_guard = True
                elif seen_guard:
                    mat[i][j] = 3  # guarded

        # Sweep columns (top -> bottom, then bottom -> top)
        for j in range(n):
            seen_guard = False
            for i in range(m):
                if mat[i][j] == 2:
                    seen_guard = False
                elif mat[i][j] == 1:
                    seen_guard = True
                elif seen_guard:
                    mat[i][j] = 3  # guarded

            seen_guard = False
            for i in range(m-1, -1, -1):
                if mat[i][j] == 2:
                    seen_guard = False
                elif mat[i][j] == 1:
                    seen_guard = True
                elif seen_guard:
                    mat[i][j] = 3  # guarded

        # Count unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    count += 1
        return count


# Notes:
# - The solution uses a grid to represent the state of each cell: unguarded (0), guard (1), wall (2), and guarded (3).
# - It performs four sweeps (left to right, right to left, top to bottom, bottom to top) to mark cells as guarded.
# - Finally, it counts the number of unguarded cells remaining in the grid.
# - Time complexity is O(m*n), where m and n are the dimensions of the grid.
# - Space complexity is O(m*n) for the grid representation.