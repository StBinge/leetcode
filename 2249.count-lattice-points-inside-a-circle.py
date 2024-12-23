#
# @lc app=leetcode.cn id=2249 lang=python3
# @lcpr version=30204
#
# [2249] 统计圆内格点数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        max_x=max_y=0
        for x,y,r in circles:
            max_x=max(max_x,x+r)
            max_y=max(max_y,y+r)
        
        dif=[[0]*(max_x+2) for _ in range(max_y+1)]
        for x,y,r in circles:
            x0=x1=x
            r2=r*r
            dif[y][x-r]+=1
            dif[y][x+r+1]-=1
            for yy in range(y-r,y):
                while (x-x0)**2 + (yy-y)**2 <= r2:
                    x0-=1
                while (x-x1)**2 + (yy-y)**2<=r2:
                    x1+=1
                dif[yy][x0+1]+=1
                dif[yy][x1]-=1
                dif[2*y-yy][x0+1]+=1
                dif[2*y-yy][x1]-=1
        
        ret=0
        for y in range(max_y+1):
            cur=0
            for x in dif[y]:
                cur+=x
                if cur>0:
                    ret+=1
        return ret
# @lc code=end
assert Solution().countLatticePoints([[2,2,2],[3,4,1]])==16
assert Solution().countLatticePoints([[2,2,1]])==5


#
# @lcpr case=start
# [[2,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,2,2],[3,4,1]]\n
# @lcpr case=end

#

