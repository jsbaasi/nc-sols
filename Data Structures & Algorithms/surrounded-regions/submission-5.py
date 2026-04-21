class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()
        for i in range(ROWS):
            if board[i][0] == "O":
                q.append((i,0))
            if board[i][COLS-1] == "O":
                q.append((i, COLS-1))
        

        for j in range(1, COLS-1):
            if board[0][j] == "O":
                q.append((0,j))
            if board[ROWS-1][j] == "O":
                q.append((ROWS-1, j))
            
        def bfs(q):
            while q:
                i, j = q.popleft()
                if (
                    0<=i<ROWS and
                    0<=j<COLS and
                    board[i][j] == "O"
                ):
                    board[i][j] = "T"
                    for dr, dc in dirs:
                        q.append((i+dr,j+dc))

        bfs(q)
        


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        