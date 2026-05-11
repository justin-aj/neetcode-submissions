from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i = 0
        a = 1
        c = []
        c.append(nums[0])
        for i in range(1, len(nums)):
            if c[-1] < nums[i]:
                c.append(nums[i])
                a += 1
            idx = bisect_left(c, nums[i])
            c[idx] = nums[i]


        print(c)
        return a
            