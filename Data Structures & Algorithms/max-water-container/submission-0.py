class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res, l, r = 0, 0, n-1
        while l<r:
            length = r-l
            height = min(heights[l], heights[r])
            res = max(res, height*length)
            if heights[l]<=heights[r]: l+=1
            else: r-=1
        return res