class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = len(nums)
        for i in range(L - 1):
            num_i = nums[i]
            for j in range(i + 1, L):
                if num_i + nums[j] == target:
                    return [i, j]
