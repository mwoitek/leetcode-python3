class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A_str = "".join([str(num) for num in A])
        A_int = int(A_str)
        ans = A_int + K
        ans_list = [int(char) for char in str(ans)]
        return ans_list
