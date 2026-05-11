class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(list(set(nums)), sorted(nums))
        if sorted(list(set(nums))) == sorted(nums):
            return False
        else:
            return True