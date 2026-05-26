class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        if L < 2:
            return None
        k = k % L
        if not k:
            return None
        nums_cp = nums[:]
        for i in range(L):
            nums[(i + k) % L] = nums_cp[i]
