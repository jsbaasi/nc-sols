class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        we do a breadth first search from the ocean edges until we
        run out of cells that are bigger than the currently visiting
        """
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = set()
        atlantic = set()
        p_queue = deque()
        a_queue = deque()
        ROWS, COLS = len(heights), len(heights[0])

        for i in range(ROWS):
            p_queue.append((i, 0))
            pacific.add((i,0))
            a_queue.append((i, COLS - 1))
            atlantic.add((i,COLS-1))

        for j in range(COLS):
            p_queue.append((0, j))
            pacific.add((0,j))
            a_queue.append((ROWS - 1, j))
            atlantic.add((ROWS-1,j))

        def bfs(q, res, visit):
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = i + dr, j + dc
                        if (
                            0 <= nr < ROWS
                            and 0 <= nc < COLS
                            and (nr,nc) not in res
                            and heights[i][j] <= heights[nr][nc]
                        ):
                            q.append((nr, nc))
                            res.add((nr,nc))

        bfs(p_queue, pacific, set())
        bfs(a_queue, atlantic, set())
        print(pacific)
        print(atlantic)

        return list(pacific.intersection(atlantic))
