class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        if len(nums1Set) > len(nums2Set):
            numsGen = (num for num in nums1Set if num in nums2Set)
        else:
            numsGen = (num for num in nums2Set if num in nums1Set)
        return [num for num in numsGen]
