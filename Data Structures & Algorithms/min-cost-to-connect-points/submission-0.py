class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, res = len(points), 0
        min_heap = [(0,0)]
        remaining = {i for i in range(n)}
        while remaining:
            while min_heap[0][1] not in remaining: heapq.heappop(min_heap)
            cost, i = heapq.heappop(min_heap)
            res+=cost; remaining.remove(i)
            for j in remaining: 
                (x0, y0), (x1, y1) = points[i], points[j]
                heapq.heappush(min_heap, (abs(x0-x1)+abs(y0-y1),j))
        return res