class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for i in range(n+1)]
        dp[0] = ['']
        for i in range(1, n+1):
            for a in range(0, i):
                for c in dp[a]:
                    for d in dp[i-a-1]:
                        dp[i].append(f"({c}){d}")
        return dp[n]
        