#
# @lc app=leetcode.cn id=1833 lang=python3
#
# [1833] 雪糕的最大数量
#
from sbw import *


# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, c in enumerate(costs):
            coins -= c
            if coins < 0:
                return i
        return len(costs)


# @lc code=end
assert Solution().maxIceCream(costs = [1,6,3,1,2,5], coins = 20) == 6
assert Solution().maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5) == 0
assert Solution().maxIceCream(costs=[1, 3, 2, 4, 1], coins=7) == 4
