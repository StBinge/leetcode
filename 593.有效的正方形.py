#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#
from typing import List
# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def check_length(v1,v2):
            return v1[0]**2+v1[1]**2==v2[0]**2+v2[1]**2
        
        def check_center(p1,p2,p3,p4):
            return p1[0]+p2[0]==p3[0]+p4[0] and p1[1]+p2[1]==p3[1]+p4[1]

        def check_perpendicular(v1,v2):
            return v1[0]*v2[0]+v1[1]*v2[1]==0
        
        def help(p1,p2,p3,p4):
            v1=[p2[0]-p1[0],p2[1]-p1[1]]
            v2=[p4[0]-p3[0],p4[1]-p3[1]]
            return check_center(p1,p2,p3,p4) and check_length(v1,v2) and check_perpendicular(v1,v2)
        if p1==p2:
            return False
        if help(p1,p2,p3,p4):
            return True
        
        if p1==p3:
            return False
        if help(p1,p3,p2,p4):
            return True
        
        if p1==p4:
            return False
        if help(p1,p4,p2,p3):
            return True
        return False

# @lc code=end

