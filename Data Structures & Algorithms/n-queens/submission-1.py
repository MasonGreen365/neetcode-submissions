class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        #sets to keep track of row, col, diag used
        #pos_diag = row + col (up and right)
        #neg_diag = row - col (down and left)
        used_cols, used_pos_diag, used_neg_diag = set(), set(), set()

        #queen col pos mapped to index
        queen_col_indices = []

        def backtrack(row):
            #base case: possible solution when end of grid
            if n == row:
                #build string result for board
                board = []
                for c in queen_col_indices:
                    dots_before = c * '.'
                    dots_after = (n-c-1) * '.'
                    row_string = dots_before + 'Q' + dots_after
                    board.append(row_string)
                solutions.append(board)

            for col in range(n):
                #is position even possible? if not, skip
                if col in used_cols or (row+col) in used_pos_diag or (row-col) in used_neg_diag: continue
                #position possible, update trackers and possible solution
                queen_col_indices.append(col)
                used_cols.add(col)
                used_pos_diag.add(row+col)
                used_neg_diag.add(row-col)

                #backtrack with updated sets
                backtrack(row + 1)

                #undo decision
                queen_col_indices.pop()
                used_cols.remove(col)
                used_pos_diag.remove(row+col)
                used_neg_diag.remove(row-col)

        backtrack(0)
        return solutions



