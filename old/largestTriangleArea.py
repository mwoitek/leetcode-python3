from itertools import combinations


def triangle_area(point_1, point_2, point_3):

    x_1 = point_1[0]
    y_1 = point_1[1]

    x_2 = point_2[0]
    y_2 = point_2[1]

    x_3 = point_3[0]
    y_3 = point_3[1]

    area = abs(0.5 * (x_1 * (y_2 - y_3) + x_2 * (y_3 - y_1) + x_3 * (y_1 - y_2)))
    return area


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        max_area = -1

        for three_points in combinations(points, 3):
            area = triangle_area(three_points[0], three_points[1], three_points[2])
            if area > max_area:
                max_area = area

        return max_area
