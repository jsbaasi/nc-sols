class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        assume we've reached the end of our recursion, what would
        it look like? what's the base case of our recursion?
        ''' 
        n = len(s)
        dp = [0] * n
        dp += [1,0]
        for i in range(n-1, -1, -1):
            fd = s[i]
            sd = s[i+1] if (i+1)<n else ""
            if fd=="0": dp[i]=0
            elif (fd=="1" or fd=="2") and sd:
                if sd=="0": dp[i]=dp[i+2]
                elif fd=="1" or "1" <= sd <= "6": dp[i]=dp[i+1]+dp[i+2]
                elif "1" <= sd <= "6": dp[i]=dp[i+1]+dp[i+2]
                else: dp[i]=dp[i+1]
            else: dp[i]=dp[i+1]
        return dp[0]
