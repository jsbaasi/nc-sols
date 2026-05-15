import copy
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def is_perm(st: str) -> bool:
            l, r = 0, len(st)-1
            while l<r:
                if st[l]==st[r]: l+=1;r-=1;
                else: return False
            return True
        
        dp = {}
        dp[-1] = [[]]
        dp[0] = [[f"{s[0]}"]]
        def dfs(i):
            print(i, dp)
            if i in dp: return dp[i]
            res = []
            for j in range(i, -1, -1):
                if is_perm(s[j:i+1]):
                    curr = copy.deepcopy(dfs(j-1))
                    for c in curr:
                        c.append(s[j:i+1])     
                    res.extend(curr)

            dp[i] = res
            return dp[i]
        return dfs(n-1)