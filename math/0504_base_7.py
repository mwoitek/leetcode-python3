class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_pos = num > 0
        num = abs(num)

        digits = []
        while num > 0:
            digits.append(num % 7)
            num //= 7

        return ("" if is_pos else "-") + "".join(str(d) for d in reversed(digits))
