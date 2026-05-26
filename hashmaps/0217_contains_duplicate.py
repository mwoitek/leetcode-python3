class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d: dict[int, int] = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        return any(v > 1 for v in d.values())
