class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()

        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
                