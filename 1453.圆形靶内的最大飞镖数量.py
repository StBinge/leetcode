#
# @lc app=leetcode.cn id=1453 lang=python3
#
# [1453] 圆形靶内的最大飞镖数量
#
from sbw import *
# @lc code=start
import math
class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def get_dis(x1,y1,x2,y2):
            return math.sqrt((x1-x2)**2+(y1-y2)**2)
        eps=1e-8
        def count(cx,cy):
            ret=0
            for i in range(L):
                x,y=darts[i]
                dis=get_dis(x,y,cx,cy)
                if dis<r+eps:
                    ret+=1
            return ret
        L=len(darts)
        ret=1
        for i in range(L-1):
            x1,y1=darts[i]
            for j in range(i+1,L):
                x2,y2=darts[j]
                dis=get_dis(x1,y1,x2,y2)
                # non point
                if dis>2*r+eps:
                    continue
                # only one point
                if abs(dis-2*r)<eps:
                    cx,cy=(x1+x2)/2,(y1+y2)/2
                    ret=max(ret,count(cx,cy))
                    continue
                # tow points

                x,y=y1-y2,x2-x1
                l_v=get_dis(x,y,0,0)
                l_f=math.sqrt(r**2-dis**2/4)
                scal=l_f/l_v
                cx,cy=(x1+x2)/2+x*scal,(y1+y2)/2+y*scal
                ret=max(ret,count(cx,cy))

                x,y=y2-y1,x1-x2
                cx,cy=(x1+x2)/2+x*scal,(y1+y2)/2+y*scal
                ret=max(ret,count(cx,cy)) 
        return ret
# @lc code=end

assert Solution().numPoints([[-2,0],[2,0],[0,2],[0,-2]],1)==1
assert Solution().numPoints(darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5)==5
assert Solution().numPoints(darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2)==4