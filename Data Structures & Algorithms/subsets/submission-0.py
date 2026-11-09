class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [],[]

        def backtrack(i):
            #base case; return result of choices
            if i == n:
                res.append(sol.copy())
                return
            
            #choice 1: don't pick nums[i]
            backtrack(i+1)
            #choice 2: pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            #backtrack: remove from solution
            sol.pop()
        backtrack(0)
        return res
            
        