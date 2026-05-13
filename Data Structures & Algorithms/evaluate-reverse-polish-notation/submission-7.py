class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+":lambda x,y: x+y,
            "-":lambda x,y: x-y,
            "*":lambda x,y: x*y,
            "/":lambda x,y: int(x/y),
        }
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in ops:
                b, a = stack.pop(), stack.pop()
                val = ops[tokens[i]](a,b)
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]