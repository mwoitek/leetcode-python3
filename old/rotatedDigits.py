rotated = {}
rotated["0"] = "0"
rotated["1"] = "1"
rotated["2"] = "5"
rotated["5"] = "2"
rotated["6"] = "9"
rotated["8"] = "8"
rotated["9"] = "6"


def is_good(num):

    global rotated

    str_num = str(num)
    str_rot = ""

    for char in str_num:
        if char not in rotated:
            return 0
        else:
            str_rot += rotated[char]

    return int(str_num != str_rot)


class Solution:
    def rotatedDigits(self, N: int) -> int:
        return sum([is_good(x) for x in range(1, N + 1)])
