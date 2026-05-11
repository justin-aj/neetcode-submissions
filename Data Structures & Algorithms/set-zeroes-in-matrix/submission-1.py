class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row, col = len(matrix), len(matrix[0])

        def make_zero(r, c):
            i = 0
            while i < row:
                print(matrix[i][c])
                matrix[i][c] = 0
                i += 1
            
            print(matrix)
            
            j = 0
            while j < col:
                print(matrix[r][j])
                matrix[r][j] = 0
                j += 1
            
            print(matrix)

        values = []

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    values.append((r, c))
        
        for vals in values:
            make_zero(vals[0], vals[1])
        