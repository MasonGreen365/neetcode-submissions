class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort by start times
        intervals.sort(key=lambda x:x[0])

        #create hashMap for lengths
        res, i = {}, 0
        #create minHeap for intervals available to each query
        minHeap = []

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r- l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]


        