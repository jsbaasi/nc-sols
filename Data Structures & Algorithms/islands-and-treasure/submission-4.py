class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    for dr, dc in dirs:
                        nr, nc = i+dr, j+dc
                        q.append((nr,nc))

        layer = 1
        max_int = (1 << 31) - 1 
        max_int = 0x7FFFFFFF
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if 0 <= i < ROWS and 0 <= j < COLS and grid[i][j]==max_int:
                    grid[i][j] = layer
                    for dr, dc in dirs:
                        nr, nc = i+dr, j+dc
                        q.append((nr,nc))
            layer+=1