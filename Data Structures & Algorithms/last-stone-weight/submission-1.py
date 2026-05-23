class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while stones and len(stones)>1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x<y: heapq.heappush_max(stones, y-x)
            elif x>y: heapq.heappush_max(stones, x-y)
            else: continue
        return stones[0] if stones else 0