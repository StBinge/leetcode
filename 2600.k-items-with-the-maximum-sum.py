#
# @lc app=leetcode.cn id=2600 lang=python3
# @lcpr version=30204
#
# [2600] K 件物品的最大和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        one=min(numOnes,k)
        neg_one=max(0,k-one-numZeros)
        return one-neg_one
# @lc code=end



#
# @lcpr case=start
# 3\n2\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n0\n4\n
# @lcpr case=end

#

