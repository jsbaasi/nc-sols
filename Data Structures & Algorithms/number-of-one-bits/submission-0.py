class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for c in bin(n)[2:]:
            res+=1 if c=="1" else 0
        return res