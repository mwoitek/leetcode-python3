class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum((1 if i % 2 == 0 else -1) * n for i, n in enumerate(nums))
