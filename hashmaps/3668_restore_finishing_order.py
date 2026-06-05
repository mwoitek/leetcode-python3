class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        fs = set(friends)
        return [i for i in order if i in fs]
