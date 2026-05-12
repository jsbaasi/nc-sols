class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        grids = {i:set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number==".": continue
                if number in rows[i]: return False
                if number in cols[j]: return False
                if number in grids[(i//3)*3+(j//3)]: return False
                grids[(i//3)*3+(j//3)].add(number)
                cols[j].add(number)
                rows[i].add(number)
        
        return True