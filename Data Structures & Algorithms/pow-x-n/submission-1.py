class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            if n==1: return x
            elif n&1: return x*rec(x*x, n//2)
            else: return rec(x*x, n//2)
        if n==0: return 1
        elif n<0: return 1/rec(x,-n)
        else: return rec(x,n)