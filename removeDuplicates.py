class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            temp = nums[i]
            j = i + 1
            while (j < len_nums) and (nums[j] == temp):
                nums.pop(j)
                len_nums -= 1
            i = j
        return len_nums
