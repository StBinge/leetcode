#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>=sx and ty>=sy:
            if tx==sx and ty==sy:
                return True
            if tx==sx:
                return (ty-sy)%sx==0
            if ty==sy:
                return (tx-sx)%sy==0
            if tx>ty:
                tx%=ty
            else:
                ty%=tx
        return False
# @lc code=end
assert Solution().reachingPoints(1,1,1000000000,1)
assert Solution().reachingPoints(1,1,3,5)
assert not Solution().reachingPoints(1,1,2,2)
assert Solution().reachingPoints(1,1,1,1)
