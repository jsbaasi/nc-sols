class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        n = len(heights)
        res = 0
        for i in range(n):
            j = len(stack)-1
            while j>=0 and stack[j][0]>heights[i]:
                res = max(res, (i-stack[j][1])*stack[j][0])
                if heights[i]!=0: stack[j][0] = heights[i]
                j-=1
            if heights[i]==0: stack.clear()
            stack.append([heights[i], i])
        for i in range(len(stack)):
            res = max(res, (n-stack[i][1])*stack[i][0])
        return res