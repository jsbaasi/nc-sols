class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sweep = defaultdict(int)
        for i in intervals:
            sweep[i.start] += 1
            sweep[i.end] -= 1
        curr = res = 0
        for t, v in sorted(sweep.items()):
            curr+=v
            res = max(res, curr)
        return res