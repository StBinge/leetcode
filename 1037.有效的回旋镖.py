#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#
from sbw import *
# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dx1,dy1=points[0][0]-points[1][0],points[0][1]-points[1][1]
        dx2,dy2=points[0][0]-points[2][0],points[0][1]-points[2][1]
        return dx1*dy2 != dx2*dy1
# @lc code=end
points = [[1,1],[2,2],[3,3]]
assert Solution().isBoomerang(points) ==False

points = [[1,1],[2,3],[3,2]]
assert Solution().isBoomerang(points)
