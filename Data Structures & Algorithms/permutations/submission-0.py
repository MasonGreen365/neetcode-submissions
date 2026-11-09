class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        #backtrack() doesn't take any arguments
        #we only need to consider elements unused; 
        #init backtrack() for every num in nums
        #append only those we don't have already in solution
        def backtrack():
            #base case: at end of list
            if len(sol) == n:
                res.append(sol.copy())
                return
            #backtracking; choice is bound; we want to start backtrack
            #at every num in nums
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return res
        