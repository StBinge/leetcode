#
# @lc app=leetcode.cn id=1465 lang=python3
#
# [1465] 切割后面积最大的蛋糕
#
from sbw import *
# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        pre=0
        max_h=0
        for cut in sorted(horizontalCuts):
            max_h=max(max_h,cut-pre)
            pre=cut
        max_h=max(max_h,h-cut)
        pre=0
        max_v=0
        for cut in sorted(verticalCuts):
            max_v=max(max_v,cut-pre)
            pre=cut
        max_v=max(max_v,w-cut)
        return (max_h*max_v)%(10**9+7)
# @lc code=end
assert Solution().maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3])==9
assert Solution().maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1])==6
assert Solution().maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3])==4
