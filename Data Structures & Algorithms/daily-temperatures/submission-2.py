class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [38, 30] 36 being considered, it's larger than 30..
        12,10,11 0, 1, 0
        [12, 10]
        '''
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i]>stack[-1][0]: res[stack[-1][1]]=i-stack[-1][1]; stack.pop()
            else: stack.append((temperatures[i], i))
        for i in range(len(stack)):
            res[stack[i][1]] = 0
        return res