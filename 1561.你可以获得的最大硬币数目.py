#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] 你可以获得的最大硬币数目
#
from sbw import *


# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles)//3::2])


# @lc code=end
assert Solution().maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18
assert Solution().maxCoins([2, 4, 5]) == 4
assert Solution().maxCoins([2, 4, 1, 2, 7, 8]) == 9
