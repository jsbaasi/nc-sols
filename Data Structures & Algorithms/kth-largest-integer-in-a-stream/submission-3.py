class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.max_heap = []
        self.k = k
        for n in nums:
            if len(self.min_heap)<k-1: heapq.heappush(self.min_heap, n)
            else:
                if k>1 and n>self.min_heap[0]: n = heapq.heapreplace(self.min_heap, n)
                heapq.heappush_max(self.max_heap, n)

    def add(self, val: int) -> int:
        if self.k > 1 and val>self.min_heap[0]:
            val = heapq.heapreplace(self.min_heap, val)
        heapq.heappush_max(self.max_heap, val)
        return self.max_heap[0]