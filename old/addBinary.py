class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if a == "0":
            return b
        elif b == "0":
            return a

        L1 = len(a)
        L2 = len(b)
        L = L2

        if L1 > L2:
            b = b.rjust(L1, "0")
            L = L1
        elif L2 > L1:
            a = a.rjust(L2, "0")

        L1 = L - 1
        sum_bin = (L + 1) * [0]

        i = L1
        while i >= 0:
            idx = L1 - i
            d1 = ord(a[i]) - 48
            d2 = ord(b[i]) - 48
            d = d1 + d2
            sum_bin[idx] += d % 2
            temp = sum_bin[idx] // 2
            sum_bin[idx] %= 2
            sum_bin[idx + 1] += d // 2 + temp
            i -= 1

        sum_bin = [str(dig) for dig in sum_bin[::-1]]
        return "".join(sum_bin).lstrip("0")
