class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def rec(a: list[int], i: int) -> None:
            ans.append(a[:])
            for j in range(i, n):
                a.append(nums[j])
                rec(a, j + 1)
                a.pop()

        rec([], 0)
        return ans
