from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        expo = round(log(n) / log(3))
        return True if n == 3 ** expo else False
