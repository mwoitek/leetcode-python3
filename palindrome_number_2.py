from math import ceil


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            digits = []
            while True:
                digits.append(x % 10)
                x //= 10
                if not x:
                    break
            temp = ceil(len(digits) / 2)
            for i in range(temp):
                if digits[i] != digits[- i - 1]:
                    return False
            return True
