from itertools import combinations_with_replacement


class Solution:
    def numSquares(self, n: int) -> int:

        i = 1
        i_sq = 1
        squares = []
        while i_sq <= n:
            squares.append(i_sq)
            i += 1
            i_sq = i * i

        if squares[-1] == n:
            return 1

        ans = 2
        idxs = [j for j in range(i - 1)]
        while True:
            for possib in combinations_with_replacement(idxs, ans):
                sum_squares = 0
                for idx in possib:
                    sum_squares += squares[idx]
                if sum_squares == n:
                    return ans
            ans += 1
