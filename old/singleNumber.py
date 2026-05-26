class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic.keys():
            if dic[key] == 1:
                return key
