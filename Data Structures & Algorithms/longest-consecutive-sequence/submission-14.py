class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        max_seq = 0

        for i, n in enumerate(nums):
            if n - 1 not in hash_map:
                element = n
                seq = 0
                while element in hash_map:
                    seq += 1
                    element += 1
                max_seq = max(max_seq, seq)
        
        return max_seq
            
                