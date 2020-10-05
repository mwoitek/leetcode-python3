class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = len(nums)
        i = 0
        while i < ans:
            if nums[i] == val:
                ans -= 1
                nums[i], nums[ans] = nums[ans], nums[i]
            else:
                i += 1
        return ans
