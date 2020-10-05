class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        dic = {}
        for i in range(3, n, 2):
            dic[i] = 1
        for i in range(3, int(n ** 0.5) + 1, 2):
            if dic[i]:
                for j in range(i * i, n, 2 * i):
                    dic[j] = 0
        count = 1
        for i in range(3, n, 2):
            count += dic[i]
        return count
