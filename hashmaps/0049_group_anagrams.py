class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: dict[str, list[str]] = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        return list(d.values())
