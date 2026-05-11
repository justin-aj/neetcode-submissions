class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        j = len(heights) - 1
        i = 0
        while i < j:
            most_water = max(most_water, ((j - i) * min(heights[i], heights[j])))
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return most_water