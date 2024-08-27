#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#
from sbw import *


# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ret = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                ret *= -1
        return ret


# @lc code=end
assert Solution().arraySign([1, 5, 0, 2, -3]) == 0
assert Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
