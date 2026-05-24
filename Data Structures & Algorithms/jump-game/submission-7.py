class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        j_max = 0
        for i, num in enumerate(nums):
            if i<=j_max: j_max = max(j_max, i+num)
        return True if j_max>=n-1 else False