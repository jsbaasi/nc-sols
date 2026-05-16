class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        we keep track of a max as we iterate through the
        the array, 
        '''
        cn = cp = nums[0]
        res = nums[0]
        length = len(nums)
        for i in range(1, length):
            n = nums[i]
            if n>0: # n is POSITIVE
                cp, cn = max(cp*n, n), min(cn*n, n)
            elif n<0: # n is NEGATIVE
                cn, cp = min(cp*n, n), max(cn*n, n)
            else:
                cn, cp = 0, 0
            res = max(res, cp, cn)
        return res