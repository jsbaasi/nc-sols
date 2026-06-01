class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        so x^2 is x*x
        x^50 is
        a=x*x (2)
        b=a*a (4)
        c=b*b (8)
        d=c*c (16)
        e=d*d (32)
        '''
        stored = {}
        def dfs(x, n):
            if n==1: return x
            elif n%2==1: stored[(x,n)] = x * dfs(x,(n-1)//2) * dfs(x,(n-1)//2)
            else: stored[(x,n)] = dfs(x,n//2) * dfs(x,n//2)
            return stored[(x,n)]
        if n==0: return 1
        elif n<0: return 1/dfs(x,-n)
        else: return dfs(x,n)
