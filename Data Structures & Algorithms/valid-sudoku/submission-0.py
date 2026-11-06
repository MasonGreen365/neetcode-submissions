class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create sets for each critera; row, col, square
        col = collections.defaultdict(set) # col number : set of seen
        row = collections.defaultdict(set) # row number : set of seen
        squares = collections.defaultdict(set) # (r//3, c//3) : set of seen
        # for X size matrix
        # skip empty spaces
        for r in range(9):
            for c in range(9):
                curr = board[r][c]

                #skip empty
                if curr == ".":
                    continue

                #check if seen
                if (curr in col[c] or
                    curr in row[r] or
                    curr in squares[(r//3, c//3)]):
                    return False
                
                #update set
                col[c].add(curr)
                row[r].add(curr)
                squares[(r//3, c//3)].add(curr)
        
        print(col)
        print(row)
        print(squares)

        return True
        