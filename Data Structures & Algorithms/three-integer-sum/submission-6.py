class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]: continue
            j,k = i+1, n-1
            while j<k:
                i_n, j_n, k_n = nums[i], nums[j], nums[k]
                curr_sum = i_n + j_n + k_n
                if j > i+1 and nums[j-1] == j_n: j+=1
                elif curr_sum<0: j+=1
                elif curr_sum>0: k-=1
                else: res.append([i_n, j_n, k_n]); j+=1
        return res