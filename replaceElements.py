def find_max_right(arr, idx, L1):
    if idx == L1:
        return -1
    right = arr[idx + 1:]
    return max(right)


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        L = len(arr)
        L1 = L - 1
        return [find_max_right(arr, idx, L1) for idx in range(L)]
