class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = False if x>0 else True
        INT_MAX = int(0x7fffffff)
        x=abs(x)
        while x:
            if res>INT_MAX//10: return 0
            res*=10
            res+=x%10
            x//=10
        return -res if neg else res