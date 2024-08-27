#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#
from sbw import *
# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ret=-1
        d=float('inf')
        for i,[a,b] in enumerate(points):
            if x!=a and y!=b:
                continue
            _d=abs(a-x)+abs(b-y)
            if _d<d:
                d=_d
                ret=i
        return ret
# @lc code=end
assert Solution().nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]])==2
