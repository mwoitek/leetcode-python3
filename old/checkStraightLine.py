class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        num_points = len(coordinates)

        if num_points == 2:
            return True

        x1 = coordinates[0][0]
        x2 = coordinates[1][0]

        if x1 == x2:
            i = 2
            while (i < num_points) and (coordinates[i][0] == x1):
                i += 1
            return i == num_points

        y1 = coordinates[0][1]
        y2 = coordinates[1][1]

        slope = (y2 - y1) / (x2 - x1)
        inter = y1 - slope * x1

        i = 2
        while i < num_points:
            x = coordinates[i][0]
            y = coordinates[i][1]
            y_line = inter + slope * x
            if y != y_line:
                return False
            i += 1
        return True
