class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        # 5,6,1,2,3,4 in sorted section
        # 3,4,5,6,1,2 in rotated section
        while l<=r:
            m = (l+r)//2
            # sorted is always to the right, rotated always left
            if nums[l]>nums[m]: # we are in the sorted section
                if nums[m]==target: return m
                elif nums[m]<target<=nums[r]: l=m+1
                else: r=m-1
            else: # we are in the rotated section
                # if target is bigger than nums[m] or smaller than nums[l] then move right
                if nums[m]==target: return m
                elif nums[l]<=target<nums[m]: r=m-1
                else: l=m+1
        return -1