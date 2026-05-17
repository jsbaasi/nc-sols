class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26
        s1_chars = set(s1)
        n, m = len(s1), len(s2)
        if n>m: return False
        for i in range(n):
            s1_count[ord(s1[i])-ord('a')]+=1
        for r in range(m):
            s2_count[ord(s2[r])-ord('a')]+=1
            if r<n-1: continue
            l=r-n+1
            if all(((True if s1_count[idx := (ord(c)) - ord("a")] == s2_count[idx] else False) for c in s1_chars)): return True
            s2_count[ord(s2[l])-ord('a')]-=1
        return False