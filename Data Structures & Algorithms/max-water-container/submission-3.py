class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        t_res = 0
        i = 0
        while i < len(heights) - 1 and j >= 0:
            dif = j - i
            res = dif * min(heights[i], heights[j])
            t_res = max(res, t_res)
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return t_res

        
