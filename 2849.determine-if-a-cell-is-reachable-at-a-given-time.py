#
# @lc app=leetcode.cn id=2849 lang=python3
# @lcpr version=30204
#
# [2849] 判断能否在给定时间到达单元格
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx=abs(sx-fx)
        dy=abs(sy-fy)
        if max(dx,dy)>t or (dx+dy==0 and t==1):
            return False
        return True
# @lc code=end



#
# @lcpr case=start
# 2\n4\n7\n7\n6\n
# @lcpr case=end

# @lcpr case=start
# 3\n1\n7\n3\n3\n
# @lcpr case=end

#

