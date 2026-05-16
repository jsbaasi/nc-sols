class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums)%2==1: return False
        target = sum(nums)//2
        dp = [[False]*(target+1) for _ in range(n+1)]
        dp[n][target] = True
        for i in range(n-1, -1, -1):
            for j in range(target, -1, -1):
                if dp[i+1][j] or ((0 <= j+nums[i] <= target) and dp[i+1][j+nums[i]]):
                    dp[i][j]=True
        return dp[0][0]