from functools import cmp_to_key


def cmp(s1: str, s2: str) -> int:
    return int(s2 + s1) - int(s1 + s2)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(n == 0 for n in nums):
            return "0"
        s = [str(n) for n in nums]
        s = sorted(s, key=cmp_to_key(cmp))
        return "".join(s)
