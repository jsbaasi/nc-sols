class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        n = len(prices)
        res = 0
        for r in range(1, n):
            if prices[l]<prices[r]: res=max(res, prices[r]-prices[l])
            else: l=r
        return res
