"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        n = len(intervals)
        curr = res = i = j = 0
        while i<n and j<n:
            if starts[i]<ends[j]: curr+=1; i+=1
            else: curr-=1; j+=1
            res = max(curr, res)
        return res