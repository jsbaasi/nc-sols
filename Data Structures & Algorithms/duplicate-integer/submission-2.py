class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set()
        for n in nums:
            if n in has: return True
            has.add(n)
        return False