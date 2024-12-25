#
# @lc app=leetcode.cn id=2679 lang=python3
# @lcpr version=30204
#
# [2679] 矩阵中的和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        return sum(max(col) for col in zip(*nums))
# @lc code=end



#
# @lcpr case=start
# [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#

