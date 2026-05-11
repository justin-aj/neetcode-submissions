class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        l = []
        for i, n in enumerate(nums):
            print(n)
            c = target - n
            print(c)
            if c in hash_map:
                return [hash_map[c], i]
            hash_map[n] = i

