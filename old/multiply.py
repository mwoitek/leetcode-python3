class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if (num1 == "0") or (num2 == "0"):
            return "0"
        elif num1 == "1":
            return num2
        elif num2 == "1":
            return num1

        L1 = len(num1) - 1
        L2 = len(num2) - 1
        prod = []

        i2 = L2
        while i2 >= 0:
            shift = L2 - i2
            L1_shift = L1 + shift
            d2 = ord(num2[i2]) - 48
            i1 = L1
            while i1 >= 0:
                idx = L1_shift - i1
                d1 = ord(num1[i1]) - 48
                d = d1 * d2
                d_rem = d % 10
                try:
                    prod[idx] += d_rem
                    temp = prod[idx] // 10
                    prod[idx] %= 10
                except IndexError:
                    prod.append(d_rem)
                    temp = 0
                temp += d // 10
                try:
                    prod[idx + 1] += temp
                except IndexError:
                    prod.append(temp)
                i1 -= 1
            i2 -= 1

        prod = [str(dig) for dig in prod[::-1]]
        return "".join(prod).lstrip("0")
