class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        res = float("inf")
        while l<=r:
            m = (l+r)//2
            if nums[m]>=nums[l]: res=min(res,nums[l]); l = m+1
            else: res=min(res,nums[m]); r = m-1
        return res