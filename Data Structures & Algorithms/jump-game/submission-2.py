class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            jump = i + nums[i]
            print(i, nums[i], jump, last)
            if jump >= last:
                last = i
        return last == 0