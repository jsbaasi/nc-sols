class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search rows then the row
        data = [matrix[i][0] for i in range(len(matrix))]
        l, r = 0, len(data)-1
        idx = -1
        while l<=r:
            m = (l+r)//2
            if data[m]<target: idx=m; l = m+1
            elif data[m]>target: r = m-1
            else: return True
        data = matrix[idx]
        l, r = 0, len(data)-1
        while l<=r:
            m = (l+r)//2
            if data[m]<target: l = m+1
            elif data[m]>target: r = m-1
            else: return True
        return False
