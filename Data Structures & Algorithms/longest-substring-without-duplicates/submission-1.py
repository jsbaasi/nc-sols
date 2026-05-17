class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        res = 0
        n = len(s)
        l = 0
        for r in range(n):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            res = max(res, r-l+1)
        return res
