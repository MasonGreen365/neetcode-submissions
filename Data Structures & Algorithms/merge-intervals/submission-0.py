class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start times
        intervals.sort(key=lambda x:x[0])
        merged = []

        for interval in intervals:
            #if we don't have an interval or last element doesnt overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            #other, there is overlap
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged

