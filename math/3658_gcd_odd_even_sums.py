from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = sum(2 * i - 1 for i in range(1, n + 1))
        sum_even = sum(2 * i for i in range(1, n + 1))
        return gcd(sum_odd, sum_even)
