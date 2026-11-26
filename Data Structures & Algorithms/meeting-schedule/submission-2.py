"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #intervals = sorted(intervals, key = lambda Interval : Interval.start)
        intervals.sort(key= lambda i:i.start)
        for i in range(len(intervals) - 1):
            #is current interval end larger than next start time?
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
