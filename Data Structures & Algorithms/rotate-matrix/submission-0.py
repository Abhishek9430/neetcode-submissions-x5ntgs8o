class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])
        if not rows==cols:
            return

        # flip on diagonal
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        # flip on middle column
        for i in range(rows):
            for j in range(cols//2):
                matrix[i][j],matrix[i][cols-j-1]=matrix[i][cols-j-1],matrix[i][j]
        