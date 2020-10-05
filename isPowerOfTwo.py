class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while not n % 2:
            n //= 2
        return not (n // 2)
