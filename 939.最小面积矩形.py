#
# @lc app=leetcode.cn id=939 lang=python3
#
# [939] 最小面积矩形
#
from sbw import *
# @lc code=start
import math
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        l=len(points)
        points_set=set(map(tuple,points))
        ret=float('inf')
        for i in range(l):
            x1,y1=points[i]
            for j in range(i+1,l):
                x2,y2=points[j]
                if x1==x2 or y1==y2:
                    continue
                if (x1,y2) in points_set and (x2,y1) in points_set:
                    ret=min(ret,abs((x2-x1)*(y2-y1)))
                            
        return 0 if math.isinf(ret) else ret
        
# @lc code=end
assert Solution().minAreaRect([[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]])==0
assert Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]])==4
assert Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])==2
