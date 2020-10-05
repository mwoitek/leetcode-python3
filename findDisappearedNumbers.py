class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        N = len(nums)
        for num in nums:
            if num not in dic:
                dic[num] = 0
        return [num for num in range(1, N + 1) if num not in dic]
