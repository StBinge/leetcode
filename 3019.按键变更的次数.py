#
# @lc app=leetcode.cn id=3019 lang=python3
#
# [3019] 按键变更的次数
#
from sbw import *
# @lc code=start
class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(x!=y for x,y in pairwise(s.lower()))
# @lc code=end
assert Solution().countKeyChanges('aAbBcC')==2
