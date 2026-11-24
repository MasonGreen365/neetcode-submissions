import heapq
class MedianFinder:

    def __init__(self):
        self.bot = [] #max heap left side of sorted array
        self.top = [] #min heap right side of sorted array

    def addNum(self, num: int) -> None:
        #insert into max heap
        heapq.heappush(self.bot, -num)
        #pop new max from maxheap and insert into min heap
        heapq.heappush(self.top, -heapq.heappop(self.bot))

        #if right side is bigger; pop min val to left side
        if len(self.top) > len(self.bot):
            heapq.heappush(self.bot, -heapq.heappop(self.top))

    def findMedian(self) -> float:
        if len(self.bot) != len(self.top):
            return -self.bot[0]
        else:
            return (self.top[0]-self.bot[0])/2
        
        