class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # grid[0][0] = grid[n-1][n-1]
        visited = set()
        min_heap = [(grid[0][0],(0,0))]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while (n-1,n-1) not in visited:
            while min_heap and min_heap[0][1] in visited: heapq.heappop(min_heap)
            cost, (i,j) = heapq.heappop(min_heap)
            visited.add((i,j))
            grid[i][j]=cost
            for dr, dc in dirs:
                if not (0<=i+dr<n and 0<=j+dc<n) or (i+dr, j+dc) in visited: continue
                heapq.heappush(min_heap, (max(grid[i][j],grid[i+dr][j+dc]), (i+dr, j+dc)))
        return grid[n-1][n-1]