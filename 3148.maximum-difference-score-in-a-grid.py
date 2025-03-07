#
# @lc app=leetcode.cn id=3148 lang=python3
# @lcpr version=30204
#
# [3148] 矩阵中的最大得分
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        f=[0]*C
        ret=float('-inf')
        for c in range(1,C):
            f[c]=grid[0][c]-grid[0][c-1]
            ret=max(ret,f[c])
            f[c]=max(f[c],0)
        for r in range(1,R):
            _f=[0]*C
            for c in range(C):
                v=grid[r][c]
                _f[c]=f[0]+v-grid[r-1][c]
                if c>0:
                    _f[c]=max(_f[c],_f[c-1]+v-grid[r][c-1])
                ret=max(ret,_f[c])
                _f[c]=max(_f[c],0)
            f=_f
        return ret
# @lc code=end

assert Solution().maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]])==9

#
# @lcpr case=start
# [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,2],[3,2,1]]\n
# @lcpr case=end

#

