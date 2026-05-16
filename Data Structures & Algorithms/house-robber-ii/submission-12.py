class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        subproblem: given maximal money for i+1 and i+2, what's maximal for i?
        state: what house we're at, how many subproblems after
        meaning: dp[i] = what's the maximal money we can rob at i
        decision: we either rob i and i+2 or i+1, as we can't rob adjacent
        transition: dp[i] = max of dp[i] + dp[i+2] OR dp[i+1]
        topo order: n...0
        base case: dp[n] = 0, house with no value gives 0 value
                    len(1) -> return value
                    len(2) -> return max()
        
        why doesn't add nums[0] to end of array work? because then we need to
        find a way to record which house we've stolen from?
        '''
        if len(nums)<=3: return max(nums)
        n = len(nums)
        nums2 = nums.copy()
        nums[-2] = max(nums[-2]+nums[0], nums[-1])
        for i in range(n-3, 1, -1):
            nums[i] = max(nums[i] + nums[i+2], nums[i+1])
        nums2[1] = max(nums2[1]+nums2[-1], nums2[0])
        for i in range(2, n-2):
            nums2[i] = max(nums2[i] + nums2[i-2], nums2[i-1])
        return max(nums[2], nums2[-3])