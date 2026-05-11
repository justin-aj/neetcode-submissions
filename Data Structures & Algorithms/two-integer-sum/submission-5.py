class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[i] + nums[j] == target:
                    return [i, j]