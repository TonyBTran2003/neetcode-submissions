class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            row_set = set()
            for value in row:
                if value != ".":
                    if value in row_set:
                        return False
                    
                    row_set.add(value)

        for col in range(9):
            col_set = set()
            for row in range(9):
                value = board[row][col]
                if value != ".":
                    if value in col_set:
                        return False

                    col_set.add(value)                    

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        value = board[row][col]

                        if value != ".":
                            if value in box_set:
                                return False

                        box_set.add(value)

        return True