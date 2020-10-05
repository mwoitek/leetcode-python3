class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp = str(- x)[::-1]
            temp = int(temp)
            return (- temp) if temp <= 2147483648 else 0
        else:
            temp = str(x)[::-1]
            temp = int(temp)
            return temp if temp <= 2147483647 else 0
