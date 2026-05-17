class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def get_idx(c: str):
            return ord(c)-ord('a')
        s1_count = [0]*26
        s2_count = [0]*26
        s1_chars = set(s1)
        need = len(s1_chars)
        matches = 0
        n, m = len(s1), len(s2)

        if n>m: return False

        for i in range(n):
            s1_count[ord(s1[i])-ord('a')]+=1

        for r in range(m):
            r_i = get_idx(s2[r])
            s2_count[r_i]+=1
            if s2[r] in s1_chars:
                if s1_count[r_i]==s2_count[r_i]: matches+=1
                elif s1_count[r_i]==s2_count[r_i]-1: matches-=1
            if r<n-1: continue
            l=r-n+1
            if matches==need: return True
            l_i = get_idx(s2[l])
            if s2[l] in s1_chars:
                if s1_count[l_i]==s2_count[l_i]: matches-=1
                elif s1_count[l_i]==s2_count[l_i]-1: matches+=1
            s2_count[l_i]-=1

        print(matches, need)
        return False if matches!=need else True