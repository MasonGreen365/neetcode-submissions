class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        #backtrack
        def backtrack(i):
            #base case: index at len s
            if i >= len(s):
                res.append(sol.copy())
                return

            #choose partition point from our curr index
            for j in range(i, len(s)):
                if validPalindrome(s, i, j):
                    sol.append(s[i : j + 1])
                    backtrack(j + 1)
                    sol.pop()
        #palindrome checker
        def validPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r  = l + 1, r - 1
            return True

        backtrack(0)
        return res