class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix.pop(0)
            
            if matrix and matrix[0]:
                for m in matrix:
                    result.append(m.pop())
            
            print(result)
            
            if matrix:
                result += matrix.pop()[::-1]
            
            print(result)
            
            if matrix and matrix[0]:
                for m in reversed(matrix):
                    result.append(m.pop(0))
        
        return result

            
            
