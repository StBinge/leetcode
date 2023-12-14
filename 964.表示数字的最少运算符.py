#
# @lc app=leetcode.cn id=964 lang=python3
#
# [964] 表示数字的最少运算符
#
from sbw import *


# @lc code=start
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cost = list(range(40))
        cost[0] = 2

        @lru_cache
        def dp(i, t):
            if t == 0:
                return 0
            if t == 1:
                return cost[i]
            if i >= 39:
                return float("inf")
            t, r = divmod(t, x)
            return min(cost[i] * r + dp(i + 1, t), cost[i] * (x - r) + dp(i + 1, t + 1))

        return dp(0, target) - 1


# @lc code=end
x = 5
target = 501
assert Solution().leastOpsExpressTarget(x, target) == 8

x = 2
target = 125046
assert Solution().leastOpsExpressTarget(x, target) == 50

x = 3
target = 19
assert Solution().leastOpsExpressTarget(x, target) == 5
