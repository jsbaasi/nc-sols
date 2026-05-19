from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]
        res = 1
        for i in range(1, n):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp): dp.append(nums[i])
            else:
                dp[idx] = min(dp[idx], nums[i])
        return len(dp)