class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, max(n-(m-i)-1, -1), -1):
                b = dp[i+1][j] if i+1<m else 0
                br = dp[i+1][j+1] if (i+1<m and j+1<n) else 1
                dp[i][j] = int(s[i]==t[j])*br+b
        print(dp)
        return dp[0][0]