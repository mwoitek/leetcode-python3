import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums = np.array(nums, dtype=np.int_)
        L = nums.size

        output = np.zeros(L, dtype=np.int_)

        idx_zeros = (nums == 0)
        num_zeros = nums[idx_zeros].size

        if num_zeros > 1:
            return output
        elif num_zeros == 1:
            output[idx_zeros] = np.prod(nums[nums != 0], dtype=np.int_)
            return output
        else:
            idx_neg = (nums < 0)
            num_neg = nums[idx_neg].size
            output = np.absolute(nums, dtype=np.int_)
            output = np.log(output, dtype=np.float_)
            ln_prod = np.sum(output, dtype=np.float_)
            output = ln_prod - output
            output = np.exp(output, dtype=np.float_)
            if num_neg > 0:
                output[idx_neg] *= -1
                output *= (-1) ** num_neg
            return np.rint(output).astype(np.int_)
