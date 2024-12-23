#
# @lc app=leetcode.cn id=2833 lang=python3
# @lcpr version=30204
#
# [2833] 距离原点最远的点
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('L')-moves.count('R'))+moves.count('_')

# @lc code=end



#
# @lcpr case=start
# "L_RL__R"\n
# @lcpr case=end

# @lcpr case=start
# "_R__LL_"\n
# @lcpr case=end

# @lcpr case=start
# "_______"\n
# @lcpr case=end

#

