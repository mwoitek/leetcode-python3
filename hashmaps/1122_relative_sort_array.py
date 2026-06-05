class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d: dict[int, int] = {}
        for n in arr1:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        ans = [0] * len(arr1)
        i = 0

        for n in arr2:
            if n not in d:
                continue
            while d[n] > 0:
                ans[i] = n
                i += 1
                d[n] -= 1
            del d[n]

        for n in sorted(d):
            while d[n] > 0:
                ans[i] = n
                i += 1
                d[n] -= 1

        return ans
