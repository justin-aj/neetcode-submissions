class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            
            print(left, right, "OK")
            print(heights[left], heights[right])
            size = min(heights[left], heights[right])
            leng = right - left
            max_water = max(max_water, size * leng)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
            
            

            
