sys.setrecursionlimit(10000)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def check_pali(i,j):
            if i<0 or j>=n or s[i]!=s[j]: return ""
            else:
                return check_pali(i-1,j+1) or s[i:j+1]

        for i in range(n):
            res = max(
                res,
                check_pali(i,i),
                check_pali(i,i+1),
                key=len
            )
        return res