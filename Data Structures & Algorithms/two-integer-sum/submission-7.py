class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, n in enumerate(nums):
            c = target - n
            if c in hash_map:
                return [hash_map[c], i]
            hash_map[n] = i

