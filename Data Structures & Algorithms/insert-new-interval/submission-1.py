class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, v in enumerate(intervals):
            ns, ne = newInterval
            s, e = v 
            if e < ns: res.append(intervals[i])
            elif ne < s: res.append(newInterval); return res+intervals[i:]
            else: newInterval = [min(s, ns), max(e, ne)]
        res.append(newInterval)
        print(res)
        return res