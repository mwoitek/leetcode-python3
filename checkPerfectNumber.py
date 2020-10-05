class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        sum_div = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                temp = num / i
                if i != temp:
                    sum_div += i + temp
                else:
                    sum_div += i
        return True if num == sum_div else False
