class Solution:
    def reverseBits(self, n: int) -> int:
        n_str = format(n, 'b')
        c = ""
        for i in range(32 - len(n_str)):
            c = c + '0'
        n_final = c + n_str
        n_rev = list(n_final)[::-1]
        n_join = "".join(n_rev)
        return int(n_join, 2)
