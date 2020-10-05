class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:].rjust(32, "0")
        bin_y = bin(y)[2:].rjust(32, "0")
        return sum([int(bin_x[i] != bin_y[i]) for i in range(32)])
