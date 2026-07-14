

class Solution:

    def isValid(self, cells):
        seen = set()
        for cell in cells:
            if cell == ".":
                continue
            if cell in seen:
                return False
            seen.add(cell)
        return True    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            if not self.isValid(board[r]):
                return False
        for c in range(9):
            column = []

            for r in range(9):
                column.append(board[r][c])

            if not self.isValid(column):
                return False

        for start_row in [0, 3, 6]:
            for start_col in [0, 3, 6]:

                box = []

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        box.append(board[r][c])

                if not self.isValid(box):
                    return False

        return True


# Have to revise it laterrr                        