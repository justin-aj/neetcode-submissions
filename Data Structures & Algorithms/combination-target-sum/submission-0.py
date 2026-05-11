class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def comb(curr, start, target):
            if target == 0:
                result.append(curr)
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                comb(curr + [nums[i]], i, target - nums[i])
        
        comb([], 0, target)
        
        return result
        