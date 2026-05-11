class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, cols = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prev_height):
            if r < 0 or c < 0 or r >= row or c >= cols or (r, c) in visit or heights[r][c] < prev_height:
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(row - 1, c, atlantic, heights[row - 1][c])

        for r in range(row):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
            
        
        
        return list(pacific & atlantic)
                