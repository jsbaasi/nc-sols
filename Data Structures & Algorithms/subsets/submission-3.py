class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for mask in range(1 << n):
            curr = []
            for i in range(n):
                if (1 << i) & mask:
                    curr.append(nums[i])
            res.append(curr)
        return res