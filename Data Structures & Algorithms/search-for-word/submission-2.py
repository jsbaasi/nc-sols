class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visit = set()
        def dfs(i: int, j: int, w: str):
            if i<0 or j<0 or i>=ROWS or j>=COLS or (i,j) in visit: return False
            w = w + board[i][j]
            if len(w)==len(word):
                if w==word: return True
                else: return False
            visit.add((i,j))
            for dr, dc in dirs:
                if dfs(i+dr, j+dc, w): return True
            visit.remove((i,j))

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, ""): return True
        return False