class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        state: pointers to where we are in each string, i and j
        decision: at each node, we have to pick, do we include a letter
        from i or j? btw the interleaving happens naturally, it's
        impossible to interleave both strings and not have a 
        | m-n|<=1. if the index of j matches and it's onward path
        matches then true and vice versa for i
        '''
        m, n, o = len(s1), len(s2), len(s3)
        if m+n!=o: return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i==m and j==n: continue
                b = (dp[i+1][j] and s1[i]==s3[i+j]) if i<m else False
                r = (dp[i][j+1] and s2[j]==s3[i+j]) if j<n else False
                dp[i][j] = b or r
        return dp[0][0]