class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range(len(nums)):
            c = nums[i]
            if target-c in find: return [find[target-c], i]
            find[c] = i
        
