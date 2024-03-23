#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#
from sbw import *
# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ret=0
        for i in range(len(points)-1):
            dx,dy=points[i][0]-points[i+1][0],points[i][1]-points[i+1][1]
            x=abs(dx)
            y=abs(dy)
            ret+=max(x,y)
        return ret
# @lc code=end
assert Solution().minTimeToVisitAllPoints([[3,2],[-2,2]])==5
assert Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])==7
