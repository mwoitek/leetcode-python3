def compute_score(s, idx):
    l_subs = s[:idx]
    r_subs = s[idx:]
    l_0 = sum([int(dig == "0") for dig in l_subs])
    r_1 = sum([int(dig == "1") for dig in r_subs])
    return l_0 + r_1


class Solution:
    def maxScore(self, s: str) -> int:
        max_score = -1
        for idx in range(1, len(s)):
            score = compute_score(s, idx)
            if score > max_score:
                max_score = score
        return max_score
