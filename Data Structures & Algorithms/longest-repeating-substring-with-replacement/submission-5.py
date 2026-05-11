class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        hash_map = defaultdict(int)
        max_freq = 0
        cons = 0
        
        while right < len(s):
            hash_map[s[right]] += 1
            max_freq = max(max_freq, hash_map[s[right]])
            if (right - left + 1) - max_freq <= k:
                cons = max(cons, right - left + 1)
            else:
                hash_map[s[left]] -= 1
                left += 1
            right += 1

        return cons

