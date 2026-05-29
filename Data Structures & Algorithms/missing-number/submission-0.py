class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n*n+1)/2
        n = len(nums)
        target = int((n*(n+1))/2)
        return target-sum(nums)