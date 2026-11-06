"""
1. given nums of length n+1 range 1,n where +1 is duplicate integer; 
    find repeated integer
    try to use o(1) space and not modify array

2. approaches:
    array is not sorted; by sorting and going through iteratively,
    can find duplicate and return immediately (o(nlogn)) but fails cond.
    other approach is to build hashMap and return any value that 
    is already in set (would be o(n)) but o(n) mem
    hints lead towards fast/slow pointers...

3. edge cases;
no None/ 0 legnth arrays so no need to avoid edges
no multi duplicated numbers so no ties
number duplicated can be 2, 3 times depending on position

comments on video; linked list problem??? value points to index, where dupicate exists is a cycle. 
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        