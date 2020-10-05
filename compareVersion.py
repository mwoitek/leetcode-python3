class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        pts1 = [int(pt) for pt in version1.split(".")]
        L1 = len(pts1)
        while (L1 > 1) and (pts1[-1] == 0):
            pts1.pop(-1)
            L1 -= 1
        pts2 = [int(pt) for pt in version2.split(".")]
        L2 = len(pts2)
        while (L2 > 1) and (pts2[-1] == 0):
            pts2.pop(-1)
            L2 -= 1
        while (L1 > 0) and (L2 > 0):
            pt1 = pts1.pop(0)
            pt2 = pts2.pop(0)
            if pt1 > pt2:
                return 1
            elif pt2 > pt1:
                return -1
            else:
                L1 -= 1
                L2 -= 1
        if L1 != 0:
            return 1
        elif L2 != 0:
            return -1
        else:
            return 0
