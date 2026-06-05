from functools import cmp_to_key


def gen_cmp(heights):
    def cmp(i, j):
        return heights[j] - heights[i]

    return cmp


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        cmp = gen_cmp(heights)
        n = len(names)
        idx = list(range(n))
        idx = sorted(idx, key=cmp_to_key(cmp))
        return [names[i] for i in idx]
