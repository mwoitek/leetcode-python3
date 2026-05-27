class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        ls = [0] * (n + 1)
        lc = 0

        for i, ch in enumerate(s, start=1):
            if ch == "L":
                lc += 1
            ls[i] = lc

        c = 0
        i = 0

        while i < n:
            j = i + 1
            while j < n and j - i + 1 != 2 * (ls[j + 1] - ls[i]):
                j += 2
            if j == n:
                break
            c += 1
            i = j + 1

        return c
