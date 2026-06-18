class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii = [ord(c) for c in s]
        n = len(s)
        return sum(abs(ascii[i] - ascii[i + 1]) for i in range(n - 1))
