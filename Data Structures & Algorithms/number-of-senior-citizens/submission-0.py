class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            res+=int(int(d[11:13])>60)
        return res