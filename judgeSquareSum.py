from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = 1
        while x <= c / x:
            x += 1
        for i in range(x):
            j = sqrt(c - i * i)
            if j == int(j):
                return True
        return False
