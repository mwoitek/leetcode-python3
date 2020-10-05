class Solution:
    def maxPower(self, s: str) -> int:

        all_different = True
        occurr = {}

        for char in s:
            if char in occurr:
                all_different = False
                occurr[char] += 1
            else:
                occurr[char] = 1

        if all_different:
            return 1

        max_power = 1
        for char in sorted(occurr, key=occurr.__getitem__, reverse=True):
            substr_len = occurr[char]
            while substr_len > 1:
                substr = "".join(char * substr_len)
                if substr in s:
                    if substr_len > max_power:
                        max_power = substr_len
                    break
                else:
                    substr_len -= 1
        return max_power
