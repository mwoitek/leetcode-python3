class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)
        l = len(candidates)

        def rec(a: list[int], s: int, i: int) -> None:
            if s == target:
                ans.append(a)
                return
            for j in range(i, l):
                c = candidates[j]
                if (new_s := s + c) > target:
                    break
                rec([*a, c], new_s, j)

        rec([], 0, 0)
        return ans
