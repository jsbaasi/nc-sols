class Solution:
    def isValid(self, s: str) -> bool:
        to_open = {
            '}':'{',
            ')':'(',
            ']':'[',
        }
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] in to_open:
                if not stack: return False
                if stack[-1]!=to_open[s[i]]: return False
                else: stack.pop()
            else:
                stack.append(s[i])
        return True if not stack else False
