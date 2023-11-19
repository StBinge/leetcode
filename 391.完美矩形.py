#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#
from typing import List
# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area,[minX,minY,maxX,maxY]=0,rectangles[0]
        cnt={}
        for x1,y1,x2,y2 in rectangles:
            area+=(x1-x2)*(y1-y2)
            minX=min(x1,minX)
            minY=min(minY,y1)
            maxX=max(maxX,x2)
            maxY=max(maxY,y2)
            for x in [x1,x2]:
                for y in [y1,y2]:
                    v=cnt.get((x,y),0)+1
                    cnt[(x,y)]=v

        
        if area!=(minX-maxX)*(minY-maxY):
            return False
        
        for x in [minX,maxX]:
            for y in [minY,maxY]:
                v=cnt.get((x,y),0)
                if v!=1:
                    return False
                del cnt[(x,y)]
        
        return all([c==2 or c==4 for c in cnt.values()])

# @lc code=end
rectangles = [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
assert Solution().isRectangleCover(rectangles)==False
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
assert Solution().isRectangleCover(rectangles)

rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
assert Solution().isRectangleCover(rectangles)==False