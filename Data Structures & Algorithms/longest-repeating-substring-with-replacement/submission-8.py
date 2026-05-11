class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        hash_map = defaultdict(int)
        max_freq = 0

        while right < len(s):
            hash_map[s[right]] += 1
            max_freq = max(hash_map.values())
            if (right - left + 1) - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1
            right += 1
        
        return right - left

