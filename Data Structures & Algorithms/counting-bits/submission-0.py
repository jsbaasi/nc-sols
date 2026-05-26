class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(n):
            res = 0
            while n:
                n &= n-1
                res+=1
            return res
        res = []
        for i in range(n+1):
            res.append(count_ones(i))
        return res