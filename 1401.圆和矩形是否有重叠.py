#
# @lc app=leetcode.cn id=1401 lang=python3
#
# [1401] 圆和矩形是否有重叠
#

# @lc code=start
# import math
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        dist=0
        if xCenter<x1 or xCenter>x2:
            dist=min((x1-xCenter)**2,(x2-xCenter)**2)
        if yCenter<y1 or yCenter>y2:
            dist+=min((y1-yCenter)**2,(y2-yCenter)**2)
        return dist<=radius**2

# @lc code=end
assert Solution().checkOverlap(radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1)==False
assert Solution().checkOverlap(1,1,1,1,-3,2,-1)==False
assert Solution().checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1)
assert Solution().checkOverlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1)
