class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        ps = self.permute(nums[1:])
        curr = []
        for p in ps:
            for i in range(len(ps[0])+1):
                here = p.copy()
                here.insert(i, nums[0])
                curr.append(here)
        return curr