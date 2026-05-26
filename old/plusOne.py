class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = "".join([str(digit) for digit in digits])
        temp = str(int(temp) + 1)
        return [int(char) for char in temp]
