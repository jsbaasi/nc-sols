class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(sorted(range(n), key=lambda i: capital[i]))
        i = 0
        prof_heap = []
        for _ in range(k):
            while i<n and capital[projects[i]]<=w:
                heapq.heappush_max(prof_heap, profits[projects[i]]); i+=1
            if not prof_heap: return w
            w+=heapq.heappop_max(prof_heap)
        return w