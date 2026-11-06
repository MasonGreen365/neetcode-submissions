# having issues ; getting confused about using set/dict/list again...
# here i tried to use set(), but we need to keep track of both 
# target AND integer. I thought i could simplify the datastruct
# by using LIST and grabbing index but you cant search list using O(1) time

# correct solution is dict(val: index) and looking up in table for each value
# o(n) to build, o(n) to search, so o(n) runtime.
# fucked up with enumerate() it returns INDEX, VALUE.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build HASHMAP
        need = {} # val -> index
        
        for i, n in enumerate(nums):
            need[n] = i
        
        # compare against nums
        for i, n in enumerate(nums):
            #calc difference
            diff = target - n
            #check if in need AND not current same as curr. index
            if diff in need and need[diff] != i:
                return [i, need[diff]]

