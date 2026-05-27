class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d: dict[str, int] = {}
        for i, c in enumerate(word):
            if c.isupper() and c in d:
                continue
            d[c] = i
        n = 0
        for c, i in d.items():
            if c.isupper():
                continue
            if (u := c.upper()) in d and d[u] > i:
                n += 1
        return n
