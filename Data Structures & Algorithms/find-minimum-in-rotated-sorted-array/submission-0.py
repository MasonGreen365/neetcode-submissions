"""
1. have sorted array where has been rotated between 1 and n (lenght of array) times

2. bst to find number times rotated; 1-n but what condition are we checking for?
l, r are pointers to 1 - n array, representing times sorted
if nums[l] > nums[r]

the array being rotated is a bit of a misnomer; we simply change our algorithm to try and find the PIVOT point (original start of sorted array)

to do this, we alter condition that we check when we calculate mid. 
we check if midpoint is greater than our right poitner; if it is, we know that the pivot point is to the right. if it isn't we know its to the left. 

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
        