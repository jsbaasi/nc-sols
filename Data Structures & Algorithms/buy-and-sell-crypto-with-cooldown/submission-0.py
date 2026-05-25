class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        at each node we take the max of:
        buying      -prices[i] + (i+1, true)    (at i, false)
        selling     +prices[i] + (i+2, false)   (at i, true)
        maintaining (i+1, true), (i+1, false)   (for both)
        base case is at i==n
        (n-1, true)     = prices[n-1]
        (n-1, false)    = 0
        '''
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = dp[n-1][0] = 0
        dp[n-1][1] = prices[n-1]
        for i in range(n-2, -1, -1):
            dp[i][0] = max(dp[i+1][1]-prices[i], dp[i+1][0])
            dp[i][1] = max(dp[i+2][0]+prices[i], dp[i+1][1])
        return dp[0][0]