#
# @lc app=leetcode.cn id=2923 lang=python3
# @lcpr version=30204
#
# [2923] 找到冠军 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for j,col in enumerate(zip(*grid)):
            if all(c==0 for c in col ):
                return j
# @lc code=end



#
# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,1],[1,0,1],[0,0,0]]\n
# @lcpr case=end

#

