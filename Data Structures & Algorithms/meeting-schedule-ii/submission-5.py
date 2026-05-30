class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = [(i.start, 1) for i in intervals] + [(i.end, -1) for i in intervals]
        heapq.heapify(min_heap)
        res = rooms = 0
        while min_heap:
            rooms+=heapq.heappop(min_heap)[1]
            res=max(res, rooms)
        return res