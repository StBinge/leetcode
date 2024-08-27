#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#
from sbw import *


# @lc code=start
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 1
        for c in coins:
            if c > x:
                break
            else:
                x+=c
        return x


# @lc code=end
assert Solution().getMaximumConsecutive([1, 1, 1, 4]) == 8
assert Solution().getMaximumConsecutive([1, 3]) == 2
