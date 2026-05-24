class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        j_max = 0
        for i, num in enumerate(nums):
            if i>j_max: return False
            elif j_max>=n-1: return True
            else: j_max = max(j_max, i+num)
        return False