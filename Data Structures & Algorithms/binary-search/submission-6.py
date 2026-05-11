from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2
            
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            # Adjust the search space
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If target is not found, return -1
        return -1
