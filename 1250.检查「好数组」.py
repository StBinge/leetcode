#
# @lc app=leetcode.cn id=1250 lang=python3
#
# [1250] 检查「好数组」
#
from sbw import *
# @lc code=start
import math
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return math.gcd(*nums)==1
# @lc code=end
assert not Solution().isGoodArray([3,6])
assert Solution().isGoodArray([12,5,7,23])
