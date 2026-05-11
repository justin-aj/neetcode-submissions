class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = {}
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]] = a[s[i]] + 1
            else:
                a[s[i]] = 1

        for i in range(len(t)):
            if t[i] in a:
                a[t[i]] = a[t[i]] - 1
                if a[t[i]] < 0:
                    return False
            else:
                return False

        return True
