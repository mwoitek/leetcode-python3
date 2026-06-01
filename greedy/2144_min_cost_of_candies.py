class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost, start=1) if i % 3 != 0)
