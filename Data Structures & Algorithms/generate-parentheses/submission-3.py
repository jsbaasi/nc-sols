class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, c, curr):
            if o==0 and c==0: res.append(curr); return
            if o<0 or c<0 or c<o: return

            dfs(o-1, c, curr+"(")
            dfs(o, c-1, curr+")")
            
        dfs(n, n, "")

        return res