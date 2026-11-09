#this solution refines my first approach, reducing constructed data structures (Trie, set(words) and resultant set() of found ones) into 2 (Trie, resultant set())
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Function buildTrie builds a Trie from List of words
        #and returns root (trie); at end of each path is word itself 
        #for quick return
        def buildTrie(words):
            root = {}
            for word in words:
                node = root
                for c in word:
                    #setdefault is function equivalent to 
                    """
                    if c not in d:
                        d[c] = {}
                    d = d[c]
                    """
                    node = node.setdefault(c, {})
                node['.'] = word
            return root

        #build Trie and get board size
        trie = buildTrie(words)
        m, n  = len(board), len(board[0])

        #build result
        res = []

        #backtracking is search function that checks against Trie 
        def backtracking(i, j, curr):
            char = board[i][j]
            board[i][j] = '#'

            if '.' in curr:
                res.append(curr.pop('.'))

            for i_off, j_off in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n and board[r][c] in curr:
                    backtracking(r, c, curr[board[r][c]])

            board[i][j] = char

        #call backtracking on every possible char if in Trie
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtracking(i, j, trie[board[i][j]])

        return res

        
        