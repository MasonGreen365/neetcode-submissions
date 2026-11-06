"""
1. rotated (1-n times) array size n where we watnt ot return target index. -1 if not

2. use bst to find target; but how do we know that it is to the left or right?
try and identify pivot point
    - if nums[m] > nums[r], we know that pivot takes place here
    - if nums[m] < nums[l], we know pivot takes place here
knowing direction of pivot, look for target value
    - move r to m if: 

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l, r = 0, n

        #find pivot point
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        #left pointer l is pivot (or Minimum)
        min_i = l

        #determine how to initialize new BST
        #is sorted array not rotated?
        if min_i == 0:
            l, r = 0, n 
        #is target to the left of pivot?
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        #is target to the right of pivot?
        else:
            l, r = min_i, n 

        #BST for remainder of array
        while l <= r:
            m = (l + r ) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
            

        