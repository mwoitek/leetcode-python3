from itertools import accumulate


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0]
        alts.extend(accumulate(gain))
        return max(alts)
