class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = Counter(t)
        window = {}
        have, need = 0, len(target)
        res = ""
        left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                # Update result if this window is smaller
                window_len = right - left + 1
                if not res or window_len < len(res):
                    res = s[left:right + 1]

                # Shrink from left
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1

        return res