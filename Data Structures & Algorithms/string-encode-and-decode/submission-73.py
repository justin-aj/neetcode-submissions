class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "||0"
        
        combined_str = "".join(strs)
        lengths = [str(len(s)) for s in strs]
        length_str = '#'.join(lengths)
        return combined_str + '|' + length_str + '|' + str(len(strs))

    def decode(self, s: str) -> List[str]:
        if s == "||0":
            return []

        parts = s.rsplit('|', 2)
        data, length_str, count = parts[0], parts[1], int(parts[2])
        lengths = list(map(int, length_str.split('#')))
        
        result = []
        i = 0
        for l in lengths:
            result.append(data[i:i+l])
            i += l
        return result
