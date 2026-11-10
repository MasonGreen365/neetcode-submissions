class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        nums.sort()

        """
        solution seems to require sorting to handle duplicate values
        is there an alternative way?

        we have to handle duplicates in nums; and have NO duplicates in result
        this means when sorted, our algo should have an edge case to handle
        """
        def backtrack(i, sol):
            #base case: end of list
            if i == n:
                res.append(sol.copy())
                return
            #choice: take current index
            sol.append(nums[i])
            backtrack(i+1, sol)
            #backtrack
            sol.pop()

            #has num already appeared in sorted nums? if so, skip.
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1

            #choice: never take this index
            backtrack(i+1, sol)

        backtrack(0, sol)
        return res
        