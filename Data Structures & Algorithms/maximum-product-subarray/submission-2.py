class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        max_val = 1
        min_val = 1
        i = 0
        while i < len(nums):
            print(nums[i])
            tmp = max_val * nums[i]
            max_val = max(min_val * nums[i], max_val * nums[i], nums[i])
            min_val = min(tmp, min_val * nums[i], nums[i])
            res = max(res, max_val, min_val)
            i += 1
        
        return res

        