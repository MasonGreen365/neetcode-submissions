class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init profit tracker
        maxP = 0

        # l = buy , r = sell
        l, r = 0, 1
        
        #two pointers move forwards in time
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

            