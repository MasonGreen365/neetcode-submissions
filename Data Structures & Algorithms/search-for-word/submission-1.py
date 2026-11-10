class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)

        if m == 1 and n == 1:
            return board[0][0] == word

        def backtrack(pos, index):
            i, j = pos
            #case: we found total word
            if index == len(word):
                return True
            #case: curent char is not in word
            if board[i][j] != word[index]:
                return False

            #case: char is in word; need to backtrack to new possible paths
            char = board[i][j]
            board[i][j] = '#'
            for i_off, j_off in [(-1,0), (1, 0), (0, 1), (0, -1)]:
                #are we in bounds?
                if 0 <= i + i_off < m and 0 <= j + j_off < n:
                    #explore possible path
                    if backtrack((i + i_off, j + j_off), index + 1):
                        return True

            #unmark visited; we didnt find possible path from here
            board[i][j] = char
            return False
        
        #call backtrack on all values in matrix
        for i in range(m):
            for j in range(n):
                if backtrack((i,j), 0):
                    return True
        return False

        #time complexity:
        # o(m*n * m*n) (go through every value of matrix; then check against every value of matrix)

        