class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for j in range(n)] for i in range(n)]
        total = n**2
        cols = defaultdict(bool)
        rows = defaultdict(bool)
        neg_diags = defaultdict(bool) # r-c
        pos_diags = defaultdict(bool) # r+c
        res = []

        def board_to_res(b):
            return ["".join(l) for l in b]
        
        def is_valid(i,j):
            return (
                not rows[i] and
                not cols[j] and
                not neg_diags[i-j] and
                not pos_diags[i+j]
            )
        
        def set_bools(i,j):
            rows[i] = True
            cols[j] = True
            neg_diags[i-j] = True
            pos_diags[i+j] = True
        
        def unset_bools(i,j):
            rows[i] = False
            cols[j] = False
            neg_diags[i-j] = False
            pos_diags[i+j] = False

        def btrack(k, queens):
            if queens==0: res.append(board_to_res(board)); return
            if k>=total: return
            for l in range(k, total-(queens-1)):
                i, j = l//n, l%n
                if is_valid(i,j):
                    board[i][j] = "Q"
                    set_bools(i,j)
                    btrack(l+1, queens-1)
                    unset_bools(i,j)
                    board[i][j] = "."
        
        btrack(0,n)
        return res