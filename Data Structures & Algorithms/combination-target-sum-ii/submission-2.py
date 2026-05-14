class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(i, combi, curr_sum):
            if curr_sum==target: res.append(combi.copy()); return
            elif i>=n or curr_sum>target: return
            combi.append(candidates[i])
            dfs(i+1, combi, curr_sum+candidates[i])
            combi.pop()
            while i<n-1 and candidates[i]==candidates[i+1]: i+=1
            dfs(i+1, combi, curr_sum)
        dfs(0, [], 0)
        return res