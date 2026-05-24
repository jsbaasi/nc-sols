class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for s, e in intervals[1:]:
            last = res[-1]
            if s<=last[1]: last[1] = max(e, last[1])
            else: res.append([s,e])
        return res
