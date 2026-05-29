from functools import cache


class Solution:
    @cache
    def digit_sum(self, n: int) -> int:
        if n < 10:
            return n
        q, r = divmod(n, 10)
        return r + self.digit_sum(q)

    def minElement(self, nums: List[int]) -> int:
        return min(self.digit_sum(n) for n in nums)
