class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #two components:
        #insert into SORTED array
        n = len(intervals)
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
        if len(intervals) == n:
            intervals.append(newInterval)


        #merge
        ret_intervals = []
        for interval in intervals:
            if not ret_intervals or ret_intervals[-1][1] < interval[0]:
                ret_intervals.append(interval)
            else:
                ret_intervals[-1] = [ret_intervals[-1][0], 
                max(ret_intervals[-1][1], interval[1])]
        return ret_intervals
        
        