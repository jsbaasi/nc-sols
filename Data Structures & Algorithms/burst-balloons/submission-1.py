class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        state: what balloons we have in consideration right now.
        so a list of numbers is our state?
        decision: calc(list.remove(num)) + nums[i-1]*num*nums[i+1]
        transition: take max of all potential decisions in list and pass up val

        state is too heavy, we pass in a list because when the balloon pops we need to
        know what it's neighbours were and what the new list of balloons will be
        how about we go the other way, we don't decide what balloon to pop, we decide
        on what balloon to pick last and then go from there?
        '''
        dp = {}
        def dfs(nums: list):
            if tuple(nums) in dp: return dp[tuple(nums)]
            n = len(nums)
            if n==1: dp[tuple(nums)] = nums[0]
            else: dp[tuple(nums)] = max(
                ((nums[i-1] if i-1>=0 else 1)*nums[i]*(nums[i+1] if i+1<n else 1) + dfs(nums[:i]+nums[i+1:]) for i in range(n))
            )
            return dp[tuple(nums)]
        return dfs(nums)