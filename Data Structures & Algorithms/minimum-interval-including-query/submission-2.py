class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q_sorted = {}
        for i in range(len(queries)):
            q_sorted[queries[i]] = i
        i = 0
        n = len(intervals)
        min_heap = []
        for q in sorted(q_sorted.keys()):
            while i<n and intervals[i][0]<=q:
                heapq.heappush(min_heap, (intervals[i][1]-intervals[i][0]+1, intervals[i][1]))
                i+=1
            while min_heap and min_heap[0][1] < q: heapq.heappop(min_heap)
            q_sorted[q] = min_heap[0][0] if min_heap else -1
        return [q_sorted[q] for q in queries]