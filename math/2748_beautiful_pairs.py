from itertools import combinations
from math import floor, gcd, log10


class Solution:
    def check_pair(self, i: int, j: int) -> bool:
        nd = floor(log10(i)) + 1
        fd = i // 10 ** (nd - 1)
        ld = j % 10
        return gcd(fd, ld) == 1

    def countBeautifulPairs(self, nums: List[int]) -> int:
        return sum(self.check_pair(i, j) for i, j in combinations(nums, 2))
