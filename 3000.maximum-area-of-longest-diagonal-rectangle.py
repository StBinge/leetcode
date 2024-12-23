#
# @lc app=leetcode.cn id=3000 lang=python3
# @lcpr version=30204
#
# [3000] 对角线最长的矩形的面积
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max([x*x+y*y,x*y] for x,y in dimensions)[1]
# @lc code=end



#
# @lcpr case=start
# [[9,3],[8,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4],[4,3]]\n
# @lcpr case=end

#

