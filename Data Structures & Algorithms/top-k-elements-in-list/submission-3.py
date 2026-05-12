class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        
        for num, count in count.items():
            heapq.heappush_max(max_heap, (count, num))

        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(max_heap)[1])
        return res