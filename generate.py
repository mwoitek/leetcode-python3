class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascal_triangle = numRows * [[]]
        pascal_triangle[0] = [1]
        for i in range(1, numRows):
            prev_row = pascal_triangle[i - 1]
            new_row = (i + 1) * [1]
            for j in range(1, i):
                new_row[j] = prev_row[j - 1] + prev_row[j]
            pascal_triangle[i] = new_row
        return pascal_triangle
