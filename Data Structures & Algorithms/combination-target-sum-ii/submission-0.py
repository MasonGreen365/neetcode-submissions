class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res, sol = [], []

        #define backtracking
        def backtrack(i, sol, currSum):
            #base case: we found target
            if currSum == target:
                res.append(sol.copy())
                return
            #base case: currSum is too big or we are at end; prune
            if currSum > target or i == n:
                return

            #choice 1: include i & update sum & solution
            sol.append(candidates[i])
            backtrack(i+1, sol, currSum + candidates[i])
            
            #backtrack, remove from solution
            sol.pop()

            #choice 2: don't include i
            #skip duplicate elements
            while i + 1 < n and candidates[i] == candidates[i+1]:
                i +=1
            backtrack(i+1, sol, currSum)

        backtrack(0, sol, 0)
        return res




        