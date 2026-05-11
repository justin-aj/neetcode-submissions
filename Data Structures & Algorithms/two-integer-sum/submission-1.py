class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 0
        while r < len(nums):
            print(l, r, nums[l] + nums[r])
            if l != r and nums[l] + nums[r] == target:
                return [l, r]
            if r == len(nums) - 1:
                l = l + 1
                r = 0
            r = r + 1