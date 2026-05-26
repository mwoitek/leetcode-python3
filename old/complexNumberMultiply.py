class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:

        pts_a = a.split("+")
        pts_a[1] = pts_a[1][:-1]

        pts_b = b.split("+")
        pts_b[1] = pts_b[1][:-1]

        num_a = [int(pt) for pt in pts_a]
        num_b = [int(pt) for pt in pts_b]

        prod = 2 * [0]
        prod[0] = num_a[0] * num_b[0] - num_a[1] * num_b[1]
        prod[1] = num_a[0] * num_b[1] + num_a[1] * num_b[0]
        prod = [str(pt) for pt in prod]

        return prod[0] + "+" + prod[1] + "i"
