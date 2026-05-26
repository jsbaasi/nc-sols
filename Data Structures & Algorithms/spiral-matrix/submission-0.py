class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        t, b, l, r = 0, ROWS-1, 0, COLS-1
        res = []
        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t+=1
            if t>b: return res
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r-=1
            if r<l: return res
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b-=1
            if b<t: return res
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l+=1
            if l>r: return res
        return res