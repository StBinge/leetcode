#
# @lc app=leetcode.cn id=2500 lang=python3
# @lcpr version=30204
#
# [2500] 删除每行中的最大值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        return sum(max(col) for col in  zip(*grid))
# @lc code=end



#
# @lcpr case=start
# [[1,2,4],[3,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[10]]\n
# @lcpr case=end

#

