def count_ones(str_num):
    count = 0
    for char in str_num:
        count += int(char == "1")
    return count


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        ones = [bin(num)[2:] for num in arr]
        ones = [count_ones(bin_num) for bin_num in ones]

        dic = {}
        for i in range(len(arr)):
            temp = ones[i]
            if temp not in dic:
                dic[temp] = [arr[i]]
            else:
                dic[temp].append(arr[i])

        i = 0
        for key in sorted(dic.keys()):
            temp = dic[key]
            L = len(temp)
            if L == 1:
                ones[i] = temp[0]
                i += 1
            else:
                ones[i:i + L] = sorted(temp)
                i += L
        return ones
