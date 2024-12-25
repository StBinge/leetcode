#
# @lc app=leetcode.cn id=3239 lang=python3
# @lcpr version=30204
#
# [3239] 最少翻转次数使二进制矩阵回文 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        ret1=0
        for row in grid:
            l,r=0,C-1
            while l<r:
                if row[l]!=row[r]:
                    ret1+=1
                l+=1
                r-=1
        
        ret2=0
        for col in zip(*grid):
            l,r=0,R-1
            while l<r:
                if col[l]!=col[r]:
                    ret2+=1
                l+=1
                r-=1
        return min(ret1,ret2)
# @lc code=end

assert Solution().minFlips( [[1,0,0],[0,0,0],[0,0,1]])==2

#
# @lcpr case=start
# [[1,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n
# @lcpr case=end

#

