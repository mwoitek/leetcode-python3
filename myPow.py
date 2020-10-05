class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                return helper(x * x, n / 2)
            else:
                return x * helper(x * x, (n - 1) / 2)
        return helper(x, n) if n >= 0 else 1 / helper(x, -n)
