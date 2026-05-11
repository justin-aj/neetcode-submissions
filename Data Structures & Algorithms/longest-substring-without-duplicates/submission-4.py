class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_max = set()
        out_max = 0

        left, right = 0, 0
        while right < len(s):

            if s[right] not in set_max:
                set_max.add(s[right])
                out_max = max(out_max, right - left + 1)
                right += 1
            else:
                set_max.remove(s[left])
                left += 1

            
        
        return out_max