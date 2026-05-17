class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, res, n = 0, 0, len(s)
        for r in range(n):
            count[ord(s[r])-ord('A')]+=1
            while (replacements:=r-l+1 - max(count))>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            res = max(res, r-l+1)
        return res