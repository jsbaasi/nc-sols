class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        it would be good to track the tallest bar in the window
        '''
        n = len(height)
        left_max = height[0]
        right_max = height[n-1]
        res, l, r = 0, 1, n-2
        while l<=r:
            l_h, r_h = height[l], height[r]
            if l_h>=left_max: left_max=l_h; l+=1; continue
            elif r_h>=right_max: right_max=r_h; r-=1; continue
            if left_max<=right_max:
                res+=left_max-l_h
                l+=1
            else:
                res+=right_max-r_h
                r-=1
        return res