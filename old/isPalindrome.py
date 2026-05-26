from re import split


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(split(r"\W+", s)).lower()
        s2 = s1[::-1]
        return True if s1 == s2 else False
