class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        we pick what goes last instead
        '''
        n = len(nums)
        nums.insert(0, 1); nums.append(1)
        dp = [[0]*(n) for _ in range(n)]
        def get_bound(l,r):
            pass
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                bounds = nums[i]*nums[j+2]
                if i==j: dp[i][j] = nums[i+1]*bounds
                else: dp[i][j] = max((
                    (0 if k==i else dp[i][k-1])+
                    (0 if k==j else dp[k+1][j])+
                    nums[k+1]*bounds for k in range(i, j+1)
                ))
        return dp[0][-1]