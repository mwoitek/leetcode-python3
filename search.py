from math import floor


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = len(nums)

        if L == 0:
            return -1

        first = nums[0]
        if L == 1:
            return -1 if first != target else 0

        i = 1
        while (i < L) and (nums[i] >= first):
            i += 1

        k = i % L
        max = nums[i - 1]
        min = nums[k]
        if (target < min) or (target > max):
            return -1

        nums_ord = L * [0]
        nums_ord[:(L - k)] = nums[k:]
        nums_ord[(L - k):] = nums[:k]

        left = 0
        right = L - 1
        while left <= right:
            middle = floor((left + right) / 2)
            temp = nums_ord[middle]
            if temp < target:
                left = middle + 1
            elif temp > target:
                right = middle - 1
            else:
                return (k + middle) % L
        return -1
