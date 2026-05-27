class Solution:
    def is_palindrome(self, s: str, l: int, r: int, remove: bool = False) -> bool:
        while l <= r and s[l] == s[r]:
            l += 1
            r -= 1
        if l > r:
            return True
        if not remove:
            return False
        return self.is_palindrome(s, l + 1, r) or self.is_palindrome(s, l, r - 1)

    def validPalindrome(self, s: str) -> bool:
        return self.is_palindrome(s, 0, len(s) - 1, remove=True)
