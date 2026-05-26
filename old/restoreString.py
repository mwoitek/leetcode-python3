class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        j = 0
        shuffled = len(s) * [""]
        for i in indices:
            shuffled[i] = s[j]
            j += 1
        return "".join(shuffled)
