#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#
from typing import List
# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
            rec1[0]>=rec2[2] or
            rec1[2]<=rec2[0] or
            rec1[1]>=rec2[3] or
            rec1[3]<=rec2[1]
        )
            
# @lc code=end
rec1=[5,15,8,18]
rec2=[0,3,7,9]
assert Solution().isRectangleOverlap(rec1,rec2)==False

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
assert Solution().isRectangleOverlap(rec1,rec2)==False

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
assert Solution().isRectangleOverlap(rec1,rec2)
