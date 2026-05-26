class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d: dict[str, int] = {}
        for c in word:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        n = 0
        for c in d:
            if c.swapcase() in d:
                n += 1
        return n // 2
