class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #print(str(len(s)), s)
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            print(j, "j")
            while s[j] != '#':
                j += 1
            print(j, "j")
            length = int(s[i:j])
            print(length, "l")
            i = j + 1
            print(i, "i")
            j = i + length
            print(s[i:j], i, j)
            res.append(s[i:j])
            i = j
            
        return res