class Solution:
    def thousandSeparator(self, n: int) -> str:
        comma_separated = "{:,}".format(n)
        dot_separated = ".".join(comma_separated.split(","))
        return dot_separated
