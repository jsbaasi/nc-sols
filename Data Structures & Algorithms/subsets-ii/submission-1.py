class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        def dfs(i, curr):
            if i>=n: res.append(curr.copy()); return

            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            while i<n-1 and nums[i]==nums[i+1]: i+=1
            dfs(i+1, curr)
        dfs(0, [])
        return res