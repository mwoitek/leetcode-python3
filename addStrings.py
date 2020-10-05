class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        if num1 == "0":
            return num2
        elif num2 == "0":
            return num1

        L1 = len(num1)
        L2 = len(num2)
        L = L2

        if L1 > L2:
            num2 = num2.rjust(L1, "0")
            L = L1
        elif L2 > L1:
            num1 = num1.rjust(L2, "0")

        L1 = L - 1
        sum_str = (L + 1) * [0]

        i = L1
        while i >= 0:
            idx = L1 - i
            d1 = ord(num1[i]) - 48
            d2 = ord(num2[i]) - 48
            d = d1 + d2
            sum_str[idx] += d % 10
            temp = sum_str[idx] // 10
            sum_str[idx] %= 10
            sum_str[idx + 1] += d // 10 + temp
            i -= 1

        sum_str = [str(dig) for dig in sum_str[::-1]]
        return "".join(sum_str).lstrip("0")
