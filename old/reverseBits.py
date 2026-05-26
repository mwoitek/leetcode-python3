class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:].rjust(32, "0")
        return int("0b" + bin_n[::-1], 2)
