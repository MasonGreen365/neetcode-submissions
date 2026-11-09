#watch for bounding errors;
# calling on trie at correct level, and incrimentally moving downwards into it
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #impliment Trie class to improve lookup:
        class Trie:
            def __init__(self):
                self.trie = {}

            #insert word into trie struct o(n)
            def insert(self, word : str) -> None:
                d = self.trie

                for c in word:
                    if c not in d:
                        d[c] = {}
                    d = d[c]
                
                d['.'] = '.'
        
        #build Trie on 'words'
        lookup = Trie()
        for word in words:
            lookup.insert(word)

        #build return set, transform words into set for duplicate control
        words = set(words)
        res_words = set()

        m, n = len(board), len(board[0]) #get size of grid

        #backtracking function that explores connected paths
        #ONLY if char exists in Trie and hasn't been seen before.
        #curr allows us to check at current level of Trie
        def backtracking(i, j, st, curr):
            # grab current letter, is string complete word?
            char = board[i][j]
            st += char
            if st in words: res_words.add(st)

            #mark position visited
            board[i][j] = '#'
            
            #get possible moves from current position (L, R, U, D)
            #init backtracking
            for i_off, j_off in [(-1,0), (1,0), (0,1), (0,-1)]:
                r, c  = i + i_off, j + j_off
                #is offset possible, not visited, and in trie?
                if 0 <= r < m and 0 <= c < n and board[r][c] != '#' and board[r][c] in curr:
                    backtracking(r, c, st, curr[board[r][c]])

            #unmark (backtrack)
            board[i][j] = char
        
        for i in range(m):
            for j in range(n):
                curr = lookup.trie
                if board[i][j] in curr: backtracking(i, j, '', curr[board[i][j]])

        return list(res_words)

        

            

            

        