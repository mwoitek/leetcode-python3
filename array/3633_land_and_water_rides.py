from itertools import product

BIG_INT = 2**31 - 1


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        l = list(zip(landStartTime, landDuration, strict=True))
        w = list(zip(waterStartTime, waterDuration, strict=True))

        ans = BIG_INT

        for pl, pw in product(l, w):
            (s1, d1), (s2, d2) = (
                (pl, pw)
                if pl[0] < pw[0] or (pl[0] == pw[0] and pl[1] < pw[1])
                else (pw, pl)
            )
            e1 = s1 + d1
            if e1 < s2:
                e1 += s2 - e1
            ans = min(ans, e1 + d2)

        return ans
