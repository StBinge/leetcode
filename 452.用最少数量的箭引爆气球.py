#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        right=points[0][1]
        ans=1
        for l,r in points[1:]:
            if l>right:
                right=r
                ans+=1
        return ans
# @lc code=end

