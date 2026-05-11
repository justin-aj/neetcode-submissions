class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for n, l in enumerate(matrix):
            matrix[n] = l[::-1]
        
        
                


