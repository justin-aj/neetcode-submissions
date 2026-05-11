class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        max_num = 0
        for num in nums:
            num_inc = 1
            if num - 1 not in nums:
                while num + 1 in nums:
                    num += 1
                    num_inc += 1
            max_num = max(max_num, num_inc)
        
        return max_num

                