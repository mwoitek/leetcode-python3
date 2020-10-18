from re import split
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(split(r"\s+", s.strip())[::-1])
