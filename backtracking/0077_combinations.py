class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def rec(a: list[int], i: int) -> None:
            if len(a) == k:
                ans.append(a[:])
                return
            for j in range(i, n + 1):
                a.append(j)
                rec(a, j + 1)
                a.pop()

        rec([], 1)
        return ans
