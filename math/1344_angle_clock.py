class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angleHour = 30.0 * hour + 0.5 * minutes
        angleMin = 6.0 * minutes
        diff = angleHour - angleMin if angleHour > angleMin else angleMin - angleHour
        diff %= 360.0
        return min(diff, 360.0 - diff)
