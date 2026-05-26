from math import log


log_4 = log(4)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        global log_4
        expo = log(num) / log_4
        return expo == int(expo)
