class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ws = s.split(" ")
        if len(pattern) != len(ws):
            return False
        d: dict[str, str] = {}
        for c, w in zip(pattern, ws, strict=True):
            if c in d and d[c] != w:
                return False
            d[c] = w
        return len(d) == len(set(d.values()))
