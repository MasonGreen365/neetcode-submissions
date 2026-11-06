"""
return length of consecutive elements in array
 n+1 should be 1 greater than n
 must run in O(n)

len(nums) < 10^5

1. min heap? could heapify entire nums then pop and check one at a time, building list resultant.
2. sort then brute force. O(nlogn * n) NOT POSSIBLE
3. hashset (value) : index
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if its start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest




