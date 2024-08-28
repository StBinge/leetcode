#
# @lc app=leetcode.cn id=1553 lang=python3
#
# [1553] 吃掉 N 个橘子的最少天数
#
from sbw import *


# @lc code=start
class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dp(x):
            if x<2:
                return x
            return min(x%2+1+dp(x//2), x%3+1+dp(x//3))
        return dp(n)

# @lc code=end
assert Solution().minDays(56) == 6
assert Solution().minDays(1) == 1
assert Solution().minDays(6) == 3
assert Solution().minDays(10) == 4
