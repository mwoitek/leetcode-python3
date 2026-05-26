import numpy as np


def test_1_num(num_arr1, arr2, d):
    absdiff = np.absolute(num_arr1 - arr2, dtype=np.int_)
    return int(absdiff[absdiff <= d].size == 0)


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = np.array(arr2, dtype=np.int_)
        tests = np.array([test_1_num(num, arr2, d) for num in arr1], dtype=np.int_)
        return np.sum(tests, dtype=np.int_)
