class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = [num for num in A if num % 2 == 0]
        odd = [num for num in A if num % 2 != 0]
        for i in range(len(A) // 2):
            di = 2 * i
            A[di] = even[i]
            A[di + 1] = odd[i]
        return A
