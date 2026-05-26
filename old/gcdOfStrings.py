def is_divisible(s, x):
    k = len(s) // len(x)
    x_repeat = "".join(k * [x])
    return s == x_repeat


def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = compute_gcd(len(str1), len(str2))
        x = str1[:gcd_len]
        return x if is_divisible(str1, x) and is_divisible(str2, x) else ""
