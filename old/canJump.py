class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        idx = last
        for i in range(last, -1, -1):
            if i + nums[i] >= idx:
                idx = i
        return idx == 0
