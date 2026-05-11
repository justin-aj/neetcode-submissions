class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        matrix = [[0] * (n + 1) for _ in range(m + 1)]

        for l in range(1, m + 1):
            for r in range(1, n + 1):
                if text1[l - 1] == text2[r - 1]:
                    matrix[l][r] = matrix[l-1][r-1] + 1
                else:
                    matrix[l][r] = max(matrix[l-1][r], matrix[l][r-1])
        
        return matrix[m][n]

