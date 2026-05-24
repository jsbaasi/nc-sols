class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for i in range(1,n):
            c = intervals[i]
            if c[0] <= res[-1][1]: res[-1][1] = max(c[1], res[-1][1])
            else: res.append(c)
        return res