class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # valMap = {} #index -> value
        # output = []
        # #lookup each value and assemble result array
        # for i, num in enumerate(nums):
        #     valMap[i] = num
        # for i in range(len(nums)):
        #     sum = valMap
        #     output.append()
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        
        


        