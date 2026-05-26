from re import split


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        dic = {}
        S_special = "".join(split(r"[a-zA-Z]+", S))
        for char in S_special:
            if char not in dic:
                dic[char] = 0

        S_letters = "".join(split(r"[^a-zA-Z]+", S))
        S_letters = S_letters[::-1]

        j = 0
        S_out = []
        for i in range(len(S)):
            if S[i] not in dic:
                S_out.append(S_letters[j])
                j += 1
            else:
                S_out.append(S[i])
        return "".join(S_out)
