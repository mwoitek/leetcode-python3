class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_nz = nums1[:m]
        L1 = m

        nums2_nz = nums2[:n]
        L2 = n

        i = 0
        while (L1 > 0) and (L2 > 0):
            if nums1_nz[0] <= nums2_nz[0]:
                nums1[i] = nums1_nz.pop(0)
                L1 -= 1
            else:
                nums1[i] = nums2_nz.pop(0)
                L2 -= 1
            i += 1
        nums1[i:] = nums2_nz[:] if L1 == 0 else nums1_nz[:]
