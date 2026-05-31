class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_zero = False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if j==0: col_zero=True
                    else: matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j==0:
                    if col_zero: matrix[i][j]=0
                elif matrix[i][0]==0 or matrix[0][j]==0: matrix[i][j]=0