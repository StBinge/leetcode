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
        mx_x=mx_y=0
        mi_x=mi_y=float('inf')
        circles.sort(key=lambda x:-x[2])
        for x,y,r in circles:
            mx_x=max(mx_x,x+r)
            mx_y=max(mx_y,y+r)
            mi_x=min(mi_x,r-x)
            mi_y=min(mi_y,r-y)
        ret=0
        for r in range(mi_x,mx_x+1):
            for c in range(mi_y,mx_y+1):
                for x,y,cen in circles:
                    if (r-x)**2 + (c-y)**2 <=cen**2:
                        ret+=1
                        break
        return ret
# @lc code=end



#
# @lcpr case=start
# [[2,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,2,2],[3,4,1]]\n
# @lcpr case=end

#

