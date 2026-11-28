"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


start = [0, 5, 15]
end = [40, 10, 20]

start[s]    0   5   15
end[e]      40  40  40
count       1   2   2

"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0

        while s < len(intervals):
            #is there meeting overlap?
            if start[s] < end[e]:
                s += 1
                count += 1
            #meeting has concluded
            else:
                e += 1
                count -= 1
            #store max 
            res = max(res, count)
        return res
        