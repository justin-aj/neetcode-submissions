class Solution:
    def reverseBits(self, n: int) -> int:
        # Format n as a 32-bit binary string, reverse it, and convert back to integer
        return int(format(n, '032b')[::-1], 2)
