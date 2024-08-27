#
# @lc app=leetcode.cn id=1884 lang=python3
#
# [1884] 鸡蛋掉落-两枚鸡蛋
#
from sbw import *
# @lc code=start
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return math.ceil((2*n+1/4)**0.5-0.5)
# @lc code=end
assert Solution().twoEggDrop(100)==14
assert Solution().twoEggDrop(2)==2
