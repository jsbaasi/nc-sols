class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        we can calculate the amount of k replacements used by:
        total(counter) - max(counter) if it's less than k then we
        keep growing the window right
        if it's more than k we shrink the window towards the right
        '''
        count = [0] * 26
        n = len(s)
        l = 0
        res = 0
        for r in range(n):
            count[ord(s[r])-ord('A')]+=1
            while (replacements:=sum(count) - max(count))>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            res = max(res, r-l+1)
        return res