class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    for dr,dc in dirs:
                        q.append((i+dr, j+dc))
        if not fresh: return 0
        if not q: return -1

        mins = 0
        while q and fresh:
            for _ in range(len(q)):
                i, j = q.popleft()
                if 0<=i<ROWS and 0<=j<COLS and grid[i][j]==1:
                    grid[i][j] = 2
                    fresh -=1
                    for dr,dc in dirs:
                        q.append((i+dr, j+dc))
            mins+=1
        return mins if fresh==0 else -1

            