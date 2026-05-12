class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        n = len(nums)
        curr = 1
        for i in range(n):
            curr *= nums[i]
            prefix.append(curr)
        curr = 1
        for i in range(n-1, -1, -1):
            curr *= nums[i]
            suffix.append(curr)
        # to get suffix you do n - index
        res = []
        print(prefix)
        print(suffix)
        for i in range(n):
            left = prefix[i-1] if (i-1)>=0 else 1
            right = suffix[n-i-2] if (n-i-2)>=0 else 1
            res.append(left*right)
        return res


