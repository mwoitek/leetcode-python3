class Solution:
    def generate_substrings(self, s, numRows):
        c = True
        n = len(s)
        i = 0
        while i < n:
            j = min(i + numRows, n)
            yield s[i:j], c
            c = not c
            i += numRows - 1

    def get_number_of_columns(self, s, numRows):
        gen = self.generate_substrings(s, numRows)
        return 1 + sum(len(ss) - 1 for ss, c in gen if not c)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        cols = self.get_number_of_columns(s, numRows)
        matrix = [[]] * numRows
        for i in range(numRows):
            matrix[i] = [""] * cols

        j = 0
        for ss, c in self.generate_substrings(s, numRows):
            if c:
                for i, ch in enumerate(ss):
                    matrix[i][j] = ch
            else:
                i = numRows - 1
                for ch in ss:
                    matrix[i][j] = ch
                    i -= 1
                    j += 1
                j -= 1

        lines = [""] * numRows
        for i in range(numRows):
            lines[i] = "".join(ch for ch in matrix[i] if len(ch) > 0)
        return "".join(lines)
