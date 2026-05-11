class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        hash_map = set()
        for i in range(len(nums)):
            seen = {}
            for j in range(len(nums)):
                if i != j:
                    a = nums[i] + nums[j]
                    b = 0 - a    
                    if b in seen:
                        print(i)
                        hash_map.add(tuple(sorted([nums[i], nums[j], b])))
                    seen[nums[j]] = j 
                    print(seen)
                

        return list(hash_map)

