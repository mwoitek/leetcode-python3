dic = {}
for i in range(1, 10):
    dic[str(i)] = chr(i + 96)
for i in range(10, 27):
    dic[str(i) + "#"] = chr(i + 96)


class Solution:
    def freqAlphabets(self, s: str) -> str:

        global dic

        i = 0
        L = len(s)
        s_out = ""

        while i < L - 2:
            if s[i + 2] == "#":
                s_out += dic[s[i:i + 3]]
                i += 3
            else:
                s_out += dic[s[i]]
                i += 1

        for char in s[i:]:
            s_out += dic[char]

        return s_out
