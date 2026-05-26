from re import split


class Solution:
    def toLowerCase(self, s: str) -> str:

        s_special = "".join(split(r"[a-zA-Z]+", s))

        dic = {}
        for char in s_special:
            if char not in dic:
                dic[char] = 0

        s_out = ""
        for char in s:
            if (char not in dic) and (ord(char) <= 90):
                s_out += chr(ord(char) + 32)
            else:
                s_out += char

        return s_out
