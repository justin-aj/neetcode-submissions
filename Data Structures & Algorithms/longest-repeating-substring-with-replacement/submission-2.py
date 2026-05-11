class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        leng = 0
        left = 0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1


            leng = max(leng, count[s[right]])

            if (right - left + 1) - leng > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
