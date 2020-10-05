class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        dk = 2 * k
        L = len(s)
        r = L % dk
        Lr = L - r

        s_out = ""
        for i in range(0, Lr, dk):
            temp = i + k
            s_out += s[i:temp][::-1] + s[temp:i + dk]
        temp = Lr + k
        s_out += s[Lr:temp][::-1] + s[temp:]
        return s_out
