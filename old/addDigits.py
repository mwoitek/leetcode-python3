class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum([int(dig) for dig in str(num)])
        return num
