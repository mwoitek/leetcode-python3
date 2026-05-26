from math import floor


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = floor((left + right) / 2)
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m
        return left
