class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split(" ")
        i = len(temp) - 1
        while temp[i] == "" and i > 0:
            i -= 1
        return len(temp[i])
