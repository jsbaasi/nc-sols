class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tl, tm, tr = target
        res = 0
        mask = 1<<2 | 1<<1 | 1<<0
        for l,m,r in triplets:
            if r==tr and l<=tl and m<=tm: res |= (1<<0)
            if m==tm and l<=tl and r<=tr: res |= (1<<1)
            if l==tl and m<=tm and r<=tr: res |= (1<<2)
        return res&mask==mask