dic = {}
dic["I"] = 1
dic["V"] = 5
dic["X"] = 10
dic["L"] = 50
dic["C"] = 100
dic["D"] = 500
dic["M"] = 1000


class Solution:
    def romanToInt(self, s: str) -> int:
        global dic
        int_conv = 0
        old_value = 0
        for char in s[::-1]:
            new_value = dic[char]
            if new_value >= old_value:
                int_conv += new_value
            else:
                int_conv -= new_value
            old_value = new_value
        return int_conv
