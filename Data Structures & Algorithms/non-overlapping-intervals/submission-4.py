class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = -float("inf")
        n = len(intervals)
        intervals.sort()
        def dfs(i, curr):
            nonlocal res
            if len(curr)>1 and curr[-2][1] > curr[-1][0]: return
            if i>=n: res=max(res,len(curr)); return
            curr.append(intervals[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        return n-res