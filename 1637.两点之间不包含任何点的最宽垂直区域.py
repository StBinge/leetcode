#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直区域
#
from sbw import *
# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        return max(x2[0] - x1[0] for x1,x2 in pairwise(points))
# @lc code=end

