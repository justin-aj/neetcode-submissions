class Solution:
    def countSubstrings(self, s: str) -> int:
        list_s = list(s)
        print(list_s)
        l = 0
        r = 1
        pals = []
        strs = ""
        for l in range(len(list_s)):
            pals.append(list_s[l])
            for r in range(l + 1, len(list_s)):
                #print(list_s[l], list_s[r])
                print(s[l:r + 1])
                if s[l:r+1] == s[l:r+1][::-1]:
                    pals.append(s[l:r + 1])

        return len(pals)
