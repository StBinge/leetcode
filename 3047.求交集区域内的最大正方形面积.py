#
# @lc app=leetcode.cn id=3047 lang=python3
#
# [3047] 求交集区域内的最大正方形面积
#
from sbw import *
# @lc code=start
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        L=len(bottomLeft)
        ret=0
        for i in range(L-1):
            x1,y1=bottomLeft[i]
            x2,y2=topRight[i]
            # cx1,cy1=(x1+x2)/2,(y1+y2)/2
            # w1=x2-x1
            # h1=y2-y1
            for j in range(i+1,L):
                x3,y3=bottomLeft[j]
                x4,y4=topRight[j]
                over_x=max(0,min(x2,x4)-max(x1,x3))
                over_y=max(0,min(y2,y4)-max(y1,y3))
                ret=max(ret,min(over_x,over_y))
                # cx2,cy2=(x3+x4)/2,(y3+y4)/2
                # w2=x4-x3
                # h2=y4-y3

                # dis_x=abs(cx1-cx2)
                # dis_y=abs(cy1-cy2)

                # over_w=max(w1+w2-dis_x,0)
        return ret*ret


# @lc code=end
assert Solution().largestSquareArea([[2,2],[3,1]],[[5,5],[5,5]])==4
assert Solution().largestSquareArea(bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]])==0
assert Solution().largestSquareArea(bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]])==1
assert Solution().largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]])==1
