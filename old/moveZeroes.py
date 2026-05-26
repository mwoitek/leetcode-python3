class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros = 0
        for num in nums:
            num_zeros += int(not num)
        L = len(nums) - num_zeros
        nums[:L] = [num for num in nums if num]
        nums[L:] = num_zeros * [0]
