class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_m = [[float("inf")]*n for _ in range(n)]
        for s,d,cost in flights:
            adj_m[s][d] = cost
        dp = [[float("inf")]*n for _ in range(k+1)]
        for j in range(n):
            dp[0][j] = adj_m[src][j]
        for i in range(k):
            for j in range(n):
                if dp[i][j]==float("inf"):continue
                for l in range(n):
                    if adj_m[j][l] == float("inf"): continue
                    dp[i+1][l] = min(dp[i+1][l], dp[i][j]+adj_m[j][l])
        res = min((dp[i][dst] for i in range(k+1)))
        return res if res!=float("inf") else -1