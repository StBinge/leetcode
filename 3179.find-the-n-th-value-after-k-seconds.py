#
# @lc app=leetcode.cn id=3179 lang=python3
# @lcpr version=30204
#
# [3179] K 秒后第 N 个元素的值
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, n-1)%(10**9+7)


# @lc code=end
assert Solution().valueAfterKSeconds(5, 3) == 35


#
# @lcpr case=start
# 4\n5\n
# @lcpr case=end

# @lcpr case=start
# 5\n3\n
# @lcpr case=end

#
