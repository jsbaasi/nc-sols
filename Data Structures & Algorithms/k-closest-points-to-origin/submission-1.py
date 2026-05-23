class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(((x)**2+(y)**2)**0.5,[x,y]) for x,y in points]
        heapq.heapify(min_heap)
        return [tup[1] for tup in (heapq.heappop(min_heap) for _ in range(k))]
