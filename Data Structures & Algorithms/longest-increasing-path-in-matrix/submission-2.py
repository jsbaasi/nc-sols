class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        def get(i, j):
            return matrix[i][j] if 0<=i<ROWS and 0<=j<COLS else -1

        dp = {}
        def dfs(i, j):
            if (i,j) in dp: return dp[(i,j)]
            if i<0 or j<0 or i>=ROWS or j>=COLS: dp[(i,j)] = 0
            else: dp[(i,j)] = max((dfs(i+dr,j+dc) if get(i+dr,j+dc)>get(i,j) else 0 for dr,dc in dirs)) + 1
            return dp[(i,j)]
        

        return max((dfs(i,j) for i in range(ROWS) for j in range(COLS)))