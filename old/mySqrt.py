class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        for i in range(20):
            ans = 0.5 * (ans + x / ans)
        return int(ans)
