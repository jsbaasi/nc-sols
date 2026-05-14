class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, combi, curr_sum):
            if curr_sum==target: res.append(combi.copy()); return
            elif i>=n or curr_sum>target: return

            combi.append(nums[i])
            dfs(i, combi, curr_sum+nums[i])
            combi.pop()
            dfs(i+1, combi, curr_sum)
        dfs(0, [], 0)
        return res