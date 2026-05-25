'''
if odd:
    j,i translates to x,y by + -(n-1)/2
i need the index values for each 4 elements. i can't do a tuple unpack
without making it messy i think
x,y = -y, x
j, i = x, y
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = COLS = len(matrix)
        if ROWS%2==1:
            offset = (ROWS-1)//2
            for i in range(offset):
                for j in range(COLS-offset):
                    x, y = j-offset, i-offset
                    prev = matrix[i][j]
                    for _ in range(4):
                        x, y = -y, x
                        j, i = x+offset, y+offset
                        prev, matrix[i][j] = matrix[i][j], prev
        else:
            offset = ROWS//2
            for i in range(offset):
                for j in range(offset):
                    x, y = j-offset, i-offset
                    prev = matrix[i][j]
                    for _ in range(4):
                        x, y = -y, x
                        j = x+offset if x<0 else x+offset-1
                        i = y+offset if y<0 else y+offset-1
                        prev, matrix[i][j] = matrix[i][j], prev