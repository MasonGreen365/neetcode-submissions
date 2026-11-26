"""
1. given intervals (list of lists) return min number intervals needed to remove to make non-overlapping result

2. intuiton: 
brute force: for unsorted array, check every interval against every other and slowly build result, incrementing when overlapping shows up
sort: 
    - two criteria to consider:
    sort by start: identifies duplicate start times 
        if we sort by start time, we should check which has shorter duration, which gives more intervals. drop other and increment to remain valid
    sort by end: identifies duplicate end times... other way around. start times simplier

"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by start time
        intervals.sort(key=lambda i:i[0])
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1 
                prevEnd = min(end, prevEnd)
        return res


        