class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, subset: list):
            if i>=n: res.append(subset.copy()); return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
        dfs(0, [])
        return res
