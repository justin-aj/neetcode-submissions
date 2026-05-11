class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        total_max = nums[0]
        for i in range(1, len(nums)):
            maxx = max(nums[i], maxx + nums[i])
            total_max = max(total_max, maxx)
        return total_max

        

