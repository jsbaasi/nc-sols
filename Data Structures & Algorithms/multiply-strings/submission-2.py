class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2): return "0"
        num1, num2 = num1[::-1], num2[::-1]
        if len(num1)>len(num2): num1, num2 = num2, num1
        m, n = len(num1), len(num2)
        res = [0]*(m+n)

        for i in range(m):
            d1 = int(num1[i])
            for j in range(n):
                d2 = int(num2[j])
                mult = d1*d2
                res[i+j]+=mult
                res[i+j+1]+=res[i+j]//10
                res[i+j]%=10
        if res[-1]==0: res.pop()
        return "".join(str(i) for i in res[::-1])