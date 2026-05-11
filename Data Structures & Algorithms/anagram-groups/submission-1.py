class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)

        for word in strs:
            c = [0] * 26
            for char in word:
                a = ord(char) - ord('a')
                c[a] += 1
            hash_map[tuple(c)].append(word)

        print(hash_map.values())
        return list(hash_map.values())