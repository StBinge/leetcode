#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
from sbw import *
# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        x0,y0=coordinates[0][0],coordinates[0][1]
        dx,dy=x0-coordinates[1][0],y0-coordinates[1][1]
        for i in range(2,len(coordinates)):
            x,y=coordinates[i]
            if dy*(x0-x) != dx*(y0-y):
                return False
        return True
# @lc code=end
assert Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])==False
assert Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
