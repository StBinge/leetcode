#
# @lc app=leetcode.cn id=2211 lang=python3
# @lcpr version=30204
#
# [2211] 统计道路上的碰撞次数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countCollisions(self, directions: str) -> int:
        s=directions.lstrip('L').rstrip('R')
        return len(s)-s.count('S')

# @lc code=end



#
# @lcpr case=start
# "RLRSLL"\n
# @lcpr case=end

# @lcpr case=start
# "LLRR"\n
# @lcpr case=end

#

