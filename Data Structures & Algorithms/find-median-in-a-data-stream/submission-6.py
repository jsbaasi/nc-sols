class MedianFinder:
    def __init__(self):
        self.min_heap = [] # top half
        self.max_heap = [] # bottom half

    def pop(self, h):
        return heapq.heappop(self.min_heap) if h==self.min_heap else heapq.heappop_max(self.max_heap)
        
    def push(self, h, val):
        return heapq.heappush(self.min_heap, val) if h==self.min_heap else heapq.heappush_max(self.max_heap, val)

    @property
    def length(self):
        return len(self.min_heap)+len(self.max_heap)
    
    @property
    def difference(self):
        return abs(len(self.min_heap)-len(self.max_heap))
    
    @property
    def bigger(self):
        return max(self.min_heap, self.max_heap, key=len)
    @property
    def smaller(self):
        return min(self.min_heap, self.max_heap, key=len)

    def addNum(self, num: int) -> None:
        if self.min_heap and num<self.min_heap[0]: heapq.heappush_max(self.max_heap, num)
        else: heapq.heappush(self.min_heap, num)
        if self.difference>1: self.push(self.smaller, self.pop(self.bigger))

    def findMedian(self) -> float:
        if self.length%2==0: return (self.min_heap[0]+self.max_heap[0])/2
        else:
            if self.min_heap and self.max_heap: return self.bigger[0]
            else: return (self.min_heap or self.max_heap)[0]