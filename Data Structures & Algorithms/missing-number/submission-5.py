class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_num = set(nums)
        print(set_num)
        for i in range(len(nums) + 1):
            if i not in set_num:
                return i
