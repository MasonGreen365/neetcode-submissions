class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #must start string with one open
        res, sol = [], []

        def backtrack(openn, close):
            #base case: no more pairs
            if len(sol) == 2*n:
                res.append(''.join(sol))
                return

            # add open '(' IF not greater than n
            if openn < n:
                sol.append('(')
                backtrack(openn + 1, close)
                sol.pop()
            # add close ')' IF we have more open brackets
            if openn > close:
                sol.append(')')
                backtrack(openn, close + 1)
                sol.pop()
            
        backtrack(0,0)
        return res
            


        #     #choice 1: close parentheses
        #     sol += ')'
        #     backtrack(o, c - 1)
        #     sol.pop()

        #     #choice 2: add another open
        #     sol += '('
        #     backtrack(o - 1, c)

        # backtrack(nOpen, nClose)
        # return res