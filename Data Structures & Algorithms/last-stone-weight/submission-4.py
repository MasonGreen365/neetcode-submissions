import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        #while heap remains, preform algo
        while len(stones) > 1:
            #grab two max stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: #reduce y and add back to heap
                heapq.heappush(stones, first - second)
        
        return 0 if not stones else abs(stones[0])
