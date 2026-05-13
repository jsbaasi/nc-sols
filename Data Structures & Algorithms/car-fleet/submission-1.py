class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed))
        stack = []
        '''
        0,1,4,7
        1,2,2,1
        [3,4.5]
        '''
        for i in range(n-1, -1, -1):
            pos, sp = cars[i]
            time = (target-pos)/sp
            if not stack or stack and stack[-1]<time: stack.append(time)
        return len(stack)