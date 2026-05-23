class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        step = 1
        q = deque()
        max_heap = [t for t in Counter(tasks).values()]
        heapq.heapify_max(max_heap)
        while max_heap or q:
            if q and q[0][1]==step: heapq.heappush_max(max_heap, q.popleft()[0])
            if max_heap:
                count = heapq.heappop_max(max_heap)
                if count>1: q.append((count-1, step+n+1))
            if not max_heap and not q: return step
            else: step += 1
