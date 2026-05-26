class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dic = {}
        dic[0] = 0
        dic[1] = 0
        dic[2] = 0
        for num in nums:
            dic[num] += 1

        i = 0
        for j in range(3):
            for k in range(dic[j]):
                nums[i] = j
                i += 1
