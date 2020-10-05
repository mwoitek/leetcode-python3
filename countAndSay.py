def generate_next_str(previous_str):
    L = len(previous_str)
    next_str = ""
    i = 0
    while i < L:
        char = previous_str[i]
        count = 1
        j = i + 1
        while (j < L) and (previous_str[j] == char):
            count += 1
            j += 1
        next_str += str(count) + char
        i += count
    return next_str


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n - 1):
            s = generate_next_str(s)
        return s
