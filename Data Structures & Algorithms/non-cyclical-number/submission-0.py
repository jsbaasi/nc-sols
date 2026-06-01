class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digit(n):
            while n:
                yield n%10
                n//=10
        def step(n):
            return sum(d**2 for d in get_digit(n))
        s = f = n
        while True:
            s = step(s)
            f = step(step(f))
            print(s, f)
            if s==1 or f==1: return True
            if f==s: return False