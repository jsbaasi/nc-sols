class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26
        n, m = len(s1), len(s2)
        if n>m: return False
        for i in range(n):
            s1_count[ord(s1[i])-ord('a')]+=1
        for r in range(m):
            s2_count[ord(s2[r])-ord('a')]+=1
            if r<n-1: continue
            l=r-n+1
            if s1_count==s2_count: return True
            s2_count[ord(s2[l])-ord('a')]-=1
        return False