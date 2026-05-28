class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        n = len(nums)
        for i in range(n - 2):
            if (s := nums[i + 1] + nums[i + 2]) > nums[i]:
                return nums[i] + s
        return 0
