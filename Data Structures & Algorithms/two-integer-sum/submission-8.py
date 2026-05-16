class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            dif = target - num
            print(dif, hashmap)
            if dif in hashmap:
                return [hashmap[dif], idx]
            hashmap[num] = idx
        
        return -1  