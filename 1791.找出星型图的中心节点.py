#
# @lc app=leetcode.cn id=1791 lang=python3
#
# [1791] 找出星型图的中心节点
#
from sbw import *
# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x1,y1=edges[0]
        x2,y2=edges[1]
        return x1 if (x1==x2 or x1==y2) else y1
        
# @lc code=end

