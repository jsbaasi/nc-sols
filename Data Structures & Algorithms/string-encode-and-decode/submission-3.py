class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        n = len(strs)
        for i in range(n):
            s = strs[i]
            res = res + f"{len(s)}#{s}" + ("#" if i<n-1 else "")
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []
        while i<n:
            start = i
            while s[i].isdigit(): i+=1
            print(start, i)
            length = int(s[start:i])
            i+=1
            res.append(s[i:i+length])
            i = i+length
            i+=1
        return res
