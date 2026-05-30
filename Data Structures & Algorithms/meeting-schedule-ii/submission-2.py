"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        final = max(intervals, key=lambda x: x.end).end if intervals else 0
        sweep = [0]*(final+1)
        for i in range(len(intervals)):
            for j in range(intervals[i].start, intervals[i].end):
                sweep[j]+=1
        return max(sweep)