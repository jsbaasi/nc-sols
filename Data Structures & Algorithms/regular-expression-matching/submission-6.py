class op:
    def __init__(self, ast, char):
        self.ast = ast
        self.char = char

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        state: indices into s and p
        decision: true if the pattern index matches string index AND everything
        else matches otherwise false
        '''
        def process_pattern(p):
            res, i, n = [], 0, len(p)
            while i<n:
                if i+1<n and p[i+1]=="*": res.append(op(True, p[i])); i+=2
                else: res.append(op(False, p[i])); i+=1
            return res

        p: list[op] = process_pattern(p)
        m, n = len(p), len(s)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True
        for i in range(m-1, -1, -1):
            for j in range(n, -1, -1):
                c_op = p[i]
                if c_op.ast and dp[i+1][j]: dp[i][j] = True
                elif j==n or not (c_op.char==s[j] or c_op.char=="."): continue
                elif c_op.ast and (dp[i+1][j+1] or dp[i][j+1]): dp[i][j] = True
                elif not c_op.ast and dp[i+1][j+1]: dp[i][j] = True
        return dp[0][0]