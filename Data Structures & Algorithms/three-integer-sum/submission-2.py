"""
nums is not sorted; two pointers ?
want to find triplet such that = 0
multiple pointers ? bst ? unsorted so what is best.
 - r pointer goes thru once
 - m pointer goes thru once
 - l pointer goes thru once
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # list of triplets
        nums.sort() # we don't care about index, want distinct trip.

        for i, a in enumerate(nums):
            #ensures a remains small
            if a > 0:
                break
            #jump ahead 1 if we have dup number
            if i > 0 and a == nums[i-1]:
                continue

            #two pointers for rem of aray
            l, r  = i + 1, len(nums) - 1
            while l < r:
                #calc sum and check against 0
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    #if 0, build triplet & check for duplicates
                    #move pointers (no duplicates)
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #if curr l = prev l, keep moving l forwards to exit
                    #duplicate values
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res