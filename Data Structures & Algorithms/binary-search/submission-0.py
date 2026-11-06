"""
nums : array of distinct/unique nums, ASC
target : integer

return nums[i] = target else -1

runtime : O(logn)

edge cases; no inf values

approach:
brute force search (1 element at a time)(O(n))
binary search algorithm (advantage; sorted array already removing O(nlogn) sort operation)
 - iterative (simple)
 - recursive (complex)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 #define bounds
        
        # binary search
        while l <= r:
            m = l + (r - l) // 2

            #checks
            if nums[m] > target:
                #move search to left half
                r = m - 1
            elif nums[m] < target:
                #move search to right half
                l = m + 1
            else:
                return m
        return -1


