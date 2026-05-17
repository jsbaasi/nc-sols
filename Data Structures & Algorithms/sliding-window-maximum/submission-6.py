class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        q = deque() # value, index leaving
        # monotonically decreasing queue
        for r in range(n):
            while q and q[-1][0]<nums[r]: q.pop()
            q.append((nums[r], r))
            if r<k-1: continue
            if q[0][1]<(r-k+1): q.popleft()
            res.append(q[0][0])
        return res