sys.setrecursionlimit(2000)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tail value, length of lis
        def get_candidate(res:list[tuple], i: int):
            lt = filter(lambda x:x[0]<nums[i], res)

            lt = list(lt)
            if not lt: return res + [(nums[i], 1)]
            max_llen = max(lt, key=lambda x:x[1])[1]
            max_lt = [min(filter(lambda x:x[1]==max_llen, lt), key=lambda x:x[0])]
            max_lt[0] = (nums[i], max_lt[0][1]+1)
            return max_lt 

        def dfs(i):
            if i==0: return [(nums[0], 1)]
            res = dfs(i-1)
            res.extend(get_candidate(res, i))
            return res
        n = len(nums)
        return max(dfs(n-1), key=lambda x:x[1])[1]