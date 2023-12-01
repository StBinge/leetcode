#
# @lc app=leetcode.cn id=850 lang=python3
#
# [850] 矩形面积 II
#
from typing import List
# @lc code=start
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ps=set()
        for rec in rectangles:
            ps.add(rec[0])
            ps.add(rec[2])
        ps=sorted(ps)
        ans=0
        for i in range(len(ps)-1):
            x1,x2=ps[i],ps[i+1]
            lines=[]
            for rec in rectangles:
                if rec[0]<=x1 and rec[2]>=x2:
                    lines.append([rec[1],rec[3]])
            lines.sort()
            l,r=-1,-1
            height=0
            for cur in lines:
                if cur[0]>r:
                    height+=r-l
                    l,r=cur
                elif cur[1]>r:
                    r=cur[1]
            height+=r-l
            ans+=height*(x2-x1)
            
        return ans%(10**9+7)


# @lc code=end
assert Solution().rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]])==6
assert Solution().rectangleArea([[0,0,1000000000,1000000000]])==49
assert Solution().rectangleArea([[0,0,1,1],[2,2,3,3]])==2
