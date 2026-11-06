"""
1. piles array where values are how many bananas in pile; given h hours to eat all of them. decide on k (banana eaten per hour) to eat all bananas. have to stay on pile each hour. want to find minimum k

2. brute force would be to iterate through and sum up total, derive equation? 
 - bst takes range over max(piles) and conducts bst on that, where
 we want to find minimum value that satisfies h
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #problem 1; is koko eating fast enough?
        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h
        
        #problem 2: how do we find correct k? BST
        #bst over range of max(k) (try every possible rate)
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            if k_works(k):
                r = k
            else:
                l = k + 1
        return r



        