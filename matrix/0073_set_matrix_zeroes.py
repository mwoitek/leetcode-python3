class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        r = [False] * m
        c = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue
                r[i] = True
                c[j] = True

        for i in (x for x in range(m) if r[x]):
            matrix[i] = [0] * n

        for j in (x for x in range(n) if c[x]):
            for i in range(m):
                matrix[i][j] = 0
