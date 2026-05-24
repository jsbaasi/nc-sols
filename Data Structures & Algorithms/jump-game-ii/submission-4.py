class Solution:
    def jump(self, nums: List[int]) -> int:
        res = start = end = 0
        n = len(nums)
        while end<n-1:
            next_end = start
            for i in range(start, end+1):
                next_end = max(next_end, nums[i]+i)
            start, end = end+1, next_end
            res+=1
        return res