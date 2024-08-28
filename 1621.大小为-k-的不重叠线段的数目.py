#
# @lc app=leetcode.cn id=1621 lang=python3
#
# [1621] 大小为 K 的不重叠线段的数目
#
from sbw import *


# @lc code=start
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n-1+k,2*k)%(10**9+7)

# @lc code=end
assert Solution().numberOfSets(30,7)==796297179
assert Solution().numberOfSets(3, 1) == 3
assert Solution().numberOfSets(4, 2) == 5
