class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = j = 0
        if m>n: return False
        while i<m and j<n:
            if t[j]==s[i]:
                i+=1
            j+=1
        return True if i==m else False