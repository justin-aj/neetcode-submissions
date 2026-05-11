class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(list(set(nums)))
        b = 0
        a = set(nums)
        for i, n in enumerate(a):
            if n - 1 not in a:
                l = 1
                while n + l in a:
                    l += 1
                b = max(b, l)
        
        return b