class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        res = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(q):
            curr = 0
            while q:
                i, j = q.popleft()
                if 0 <= i < ROWS and 0 <= j < COLS and grid[i][j]==1:
                    grid[i][j] = 0
                    curr+=1
                    for dr, dc in dirs:
                        nr, nc = i+dr, j+dc
                        q.append((nr,nc))
            return curr
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    q.append((i,j))
                    res = max(res, bfs(q))
        
        return res