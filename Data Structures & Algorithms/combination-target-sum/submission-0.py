class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [],[]

        def backtrack(i, currSum):
            #base case: solution found
            if currSum == target:
                res.append(sol.copy())
                return
            #base case: currSum too big/at end of array
            if currSum > target or i == n:
                return

            #choice 1: dont use i
            backtrack(i + 1, currSum)
            #choice 2: use i
            # WE DONT SKIP I because DUPLICATES ALLOWED
            sol.append(nums[i])
            backtrack(i, currSum + nums[i])

            #backtrack
            sol.pop()
        
        backtrack(0, 0)
        return res

            