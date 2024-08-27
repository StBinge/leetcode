#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#
from sbw import *
# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len=max(map(min,rectangles))
        ret= sum(x>=max_len and y>=max_len for x,y in rectangles)
        return ret
# @lc code=end
assert Solution().countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])==3
