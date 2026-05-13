class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def get_time(speed):
            time = 0
            for i in range(len(piles)):
                time+=math.ceil(piles[i]/speed)
            return time

        res = 0
        while l<=r:
            m = (l+r)//2
            m_t = get_time(m)
            if m_t>h: l=m+1
            else: res=m; r=m-1

        return res