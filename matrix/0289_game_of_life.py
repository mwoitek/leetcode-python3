class Solution:
    def count_live_neighbors(self, board: list[list[int]], i: int, j: int) -> int:
        i_min = max(i - 1, 0)
        i_max = min(i + 1, len(board) - 1)

        j_min = max(j - 1, 0)
        j_max = min(j + 1, len(board[0]) - 1)

        cnt = 0

        for r in range(i_min, i_max + 1):
            for c in range(j_min, j_max + 1):
                cnt += board[r][c]

        return cnt - board[i][j]

    def get_new_state(self, board: list[list[int]], i: int, j: int) -> int:
        n = self.count_live_neighbors(board, i, j)
        t = n == 3 if board[i][j] == 0 else n in (2, 3)
        return int(t)

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        s = [[]] * m
        for i in range(m):
            s[i] = [0] * n
            for j in range(n):
                s[i][j] = self.get_new_state(board, i, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = s[i][j]
