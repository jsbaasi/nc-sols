class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target<-total or target>total: return 0
        n = len(nums)
        ends = 2*total+1
        dp = [[0]*ends for _ in range(n)]
        dp[0][total-nums[0]] += 1
        dp[0][total+nums[0]] += 1
        for i in range(1, n):
            for j in range(ends):
                num = nums[i]
                l = dp[i-1][j-num] if j-num>=0 else 0
                r = dp[i-1][j+num] if j+num<ends else 0
                dp[i][j] = l+r
        return dp[-1][total+target]