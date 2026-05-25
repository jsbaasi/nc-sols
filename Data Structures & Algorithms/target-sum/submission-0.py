class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        def dfs(i, curr):
            if i==n: return 1 if curr==target else 0
            return dfs(i+1, curr-nums[i])+dfs(i+1, curr+nums[i])
        return dfs(0, 0)