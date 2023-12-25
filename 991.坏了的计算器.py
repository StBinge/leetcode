#
# @lc app=leetcode.cn id=991 lang=python3
#
# [991] 坏了的计算器
#
from sbw import *


# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ret = 0
        while target > startValue:
            if target % 2:
                ret += 1
            target = (target + 1) // 2
            ret += 1
        return ret + startValue - target


# @lc code=end
assert Solution().brokenCalc(3, 10) == 3
assert Solution().brokenCalc(2, 3) == 2
assert Solution().brokenCalc(5, 8) == 2
