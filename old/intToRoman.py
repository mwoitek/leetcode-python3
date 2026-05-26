dic = {}
dic[1] = "I"
dic[4] = "IV"
dic[5] = "V"
dic[9] = "IX"
dic[10] = "X"
dic[40] = "XL"
dic[50] = "L"
dic[90] = "XC"
dic[100] = "C"
dic[400] = "CD"
dic[500] = "D"
dic[900] = "CM"
dic[1000] = "M"


def find_next_digit(num):
    global dic
    for key in dic.keys():
        if key > num:
            break
        else:
            digit_value = key
            next_digit = dic[key]
    return digit_value, next_digit


class Solution:
    def intToRoman(self, num: int) -> str:
        str_out = ""
        while num > 0:
            digit_value, next_digit = find_next_digit(num)
            num -= digit_value
            str_out += next_digit
        return str_out
