class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        if we don't have a match we keep growing the string to the right
        if we have a match we shrink it left and record the length and string
        '''
        n, m = len(s), len(t)
        if m>n: return ""
        count_t = Counter(t)
        count_s = defaultdict(int)
        need = len(count_t)
        l = matches = 0
        res_len = n+1
        res = ""
        for r in range(n):
            count_s[s[r]]+=1
            if count_s[s[r]]==count_t[s[r]]: matches+=1
            while matches==need:
                if r-l+1<res_len:
                    res_len = r-l+1
                    res = s[l:r+1]
                count_s[s[l]]-=1
                if count_s[s[l]]+1==count_t[s[l]]: matches-=1
                l+=1
        return res