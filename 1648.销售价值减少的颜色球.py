#
# @lc app=leetcode.cn id=1648 lang=python3
#
# [1648] 销售价值减少的颜色球
#
from sbw import *


# @lc code=start
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        Mod = 10**9 + 7
        l, r = 0, max(inventory)
        target = 0
        remain = 0
        while l <= r:
            mid = (l + r) // 2
            if sum(inv - mid for inv in inventory if inv > mid) <= orders:
                target = mid
                r = mid - 1
            else:
                l = mid + 1
        remain = orders - sum(inv - target for inv in inventory if inv > target)
        ret = 0
        for inv in inventory:
            if inv <= target:
                continue

            ret += (inv - target) * (inv + target + 1) // 2
            ret %= Mod
        return (ret + remain * target)%Mod


# @lc code=end

assert Solution().maxProfit(inventory=[2, 5], orders=4) == 14
assert Solution().maxProfit(inventory=[2, 8, 4, 10, 6], orders=20) == 110
assert Solution().maxProfit(inventory=[1000000000], orders=1000000000) == 21
assert Solution().maxProfit(inventory=[3, 5], orders=6) == 19
