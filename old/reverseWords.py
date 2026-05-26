class Solution:
    def reverseWords(self, s: str) -> str:
        s_out = ""
        words = s.split(" ")
        for word in words:
            s_out += word[::-1] + " "
        return s_out[:-1]
