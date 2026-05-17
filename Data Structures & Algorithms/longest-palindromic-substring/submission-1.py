class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        '''
        # check single char
        n = len(s)
        res_max = 1
        res = s[0]
        def check_pali(l,r):
            nonlocal res_max, res
            while l>=0 and r<n:
                curr_len = r-l+1
                if s[l]!=s[r]: break
                if curr_len>res_max: res_max=curr_len; res=s[l:r+1]
                l-=1; r+=1

        for i in range(n):
            check_pali(i,i)
            check_pali(i,i+1)
            
        return res