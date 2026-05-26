class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        L = len(A)

        i = 0
        while (i < L) and (A[i] < 0):
            i += 1

        if i == L:
            return [x * x for x in A[::-1]]

        neg = A[:i]
        L_neg = i
        sq_neg = [x * x for x in neg[::-1]]

        non_neg = A[i:]
        L_non_neg = L - L_neg
        sq_non_neg = [x * x for x in non_neg]

        A_sq = L * [0]
        i = 0
        while (L_neg > 0) and (L_non_neg > 0):
            if sq_neg[0] <= sq_non_neg[0]:
                A_sq[i] = sq_neg.pop(0)
                L_neg -= 1
            else:
                A_sq[i] = sq_non_neg.pop(0)
                L_non_neg -= 1
            i += 1
        A_sq[i:] = sq_non_neg[:] if L_neg == 0 else sq_neg[:]
        return A_sq
