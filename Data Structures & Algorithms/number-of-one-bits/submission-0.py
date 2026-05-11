class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n))
        val = list(str(bin(n))[2:])
        print(val)
        c = Counter(val)
        return c['1']