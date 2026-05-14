class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i, combi, curr_sum):
            if curr_sum==target: res.append(combi.copy()); return
            elif i>=n or curr_sum>target: return

            for j in range(i, n):
                combi.append(nums[j])
                dfs(j, combi, curr_sum+nums[j])
                combi.pop()

        dfs(0, [], 0)
        return res