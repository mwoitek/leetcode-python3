dic = {}
dic["0"] = "1"
dic["1"] = "0"


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        global dic
        bin_N = bin(N)[2:]
        compl = "".join([dic[char] for char in bin_N])
        return int("0b" + compl, 2)
