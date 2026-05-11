class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(list(set(nums)))
        j = 0
        for element in list(set(nums)):
            print(element, "ele")
            val = element - 1
            print(val, nums)
            if val not in nums:
                l = 0
                while element + l in nums:
                    l = l + 1
                j = max(l, j)
        return j
