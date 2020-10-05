class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        return sum([int(dig == "1") for dig in bin_n])
