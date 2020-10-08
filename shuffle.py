class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffledList = 2 * n * [0]
        j = 0
        for i in range(n):
            shuffledList[j] = nums[i]
            shuffledList[j + 1] = nums[i + n]
            j += 2
        return shuffledList
