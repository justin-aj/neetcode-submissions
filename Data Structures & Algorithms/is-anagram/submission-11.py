class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = defaultdict(int)
        for i in range(len(s)):
            if hash_map[s[i]]:
                hash_map[s[i]] = hash_map[s[i]] + 1
            else:
                hash_map[s[i]] = 1
        print(hash_map)

        for i in range(len(t)):
            print(hash_map[t[i]])
            if hash_map[t[i]]:
                hash_map[t[i]] = hash_map[t[i]] - 1
            else:
                return False
        
        print(hash_map)

        return True
    
        
