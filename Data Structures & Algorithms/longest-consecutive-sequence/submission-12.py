class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = defaultdict(list)

        for i, n in enumerate(nums):
            hash_map[n].append(i)

        print(hash_map)

        seq = 0
        max_seq = 0

        for i, n in enumerate(nums):
            element = n
            seq = 0
            while hash_map[element]:
                seq += 1
                element += 1
            max_seq = max(max_seq, seq)
        
        return max_seq
            
                