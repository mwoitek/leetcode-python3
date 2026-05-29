# Surely, there's a more Pythonic way to solve this problem. However, I believe
# the "spirit" of the problem was to solve it with minimum assistance from the
# language. And that's what I did.

MIN_INT = -(2**31)
MAX_INT = 2**31 - 1
ZERO = ord("0")


class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0

        # skip leading whitespace
        while i < n and s[i] == " ":
            i += 1
        # found nothing but whitespace
        if i == n:
            return 0

        # current character should be the sign or the first digit
        # if that's not the case, then we don't have a valid integer
        if s[i] not in ("-", "+") and not s[i].isdigit():
            return 0

        # if there's a sign, consume it and then advance
        sign = "+"
        if not s[i].isdigit():
            sign = s[i]
            i += 1

        # current character should be the first digit
        # if that's not the case, then we don't have a valid integer
        if i == n or not s[i].isdigit():
            return 0

        # skip leading zeros
        while i < n and s[i] == "0":
            i += 1

        # current character should be the first non-zero digit
        # if that's not the case, then the number is zero or invalid
        if i == n or not s[i].isdigit():
            return 0

        # current character is the first non-zero digit
        # get the longest valid substring that starts at this point
        j = i + 1
        while j < n and s[j].isdigit():
            j += 1

        # now we have a valid string of digits
        # do the actual conversion
        num = 0
        p10 = 1 if sign == "+" else -1

        for k in range(j - 1, i - 1, -1):
            v = p10 * (ord(s[k]) - ZERO)
            if v > 0 and num > MAX_INT - v:
                return MAX_INT
            if v < 0 and num < MIN_INT - v:
                return MIN_INT
            num += v
            p10 *= 10

        return num
