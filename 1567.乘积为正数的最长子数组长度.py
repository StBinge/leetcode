#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] 乘积为正数的最长子数组长度
#
from sbw import *


# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ret = 0
        pos = neg = 0

        for n in nums:
            if n > 0:
                _pos = pos + 1
                _neg = (1 + neg) if neg > 0 else 0
            elif n < 0:
                _pos = (1 + neg) if neg > 0 else 0
                _neg = pos + 1
            else:
                _pos = _neg = 0
            ret = max(ret, _pos)
            pos = _pos
            neg = _neg
        return ret


# @lc code=end
assert Solution().getMaxLen([1]) == 1
assert Solution().getMaxLen([-1, -2, -3, 0, 1]) == 2
assert Solution().getMaxLen([0, 1, -2, -3, -4]) == 3
assert Solution().getMaxLen([1, -2, -3, 4]) == 4
