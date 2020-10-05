from math import floor


def bsearch(nums, target):

    left = 0
    right = len(nums) - 1

    max_nums = nums[right]
    min_nums = nums[left]
    if (target < min_nums) or (target > max_nums):
        return -1

    while left <= right:
        middle = floor((left + right) / 2)
        num_middle = nums[middle]
        if num_middle < target:
            left = middle + 1
        elif num_middle > target:
            right = middle - 1
        else:
            return middle
    return -1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        compl = target - numbers[0]
        i = 0
        L = len(numbers) - 1

        while (i < L) and (compl >= numbers[i]):
            temp = bsearch(numbers[i + 1:], compl)
            if temp != -1:
                i += 1
                temp += 1
                return [i, i + temp]
            i += 1
            compl = target - numbers[i]
