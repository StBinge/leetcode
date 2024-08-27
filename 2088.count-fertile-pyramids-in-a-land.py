#
# @lc app=leetcode.cn id=2088 lang=python3
# @lcpr version=30204
#
# [2088] 统计农场中肥沃金字塔的数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dp():
            f0=grid[-1].copy()
            ret=0
            for r in range(R-2,-1,-1):
                f1=grid[r].copy()
                for c in range(1, C-1):
                    if grid[r][c] == 1:
                        f1[c]=min(f0[c-1],f0[c],f0[c+1])+1
                        ret+=f1[c]-1
                f0=f1
            return ret
        ret=dp()
        for r in range(R//2):
            grid[r],grid[-1-r]=grid[-1-r],grid[r]
        ret+=dp()
        return ret




# @lc code=end

assert Solution().countPyramids([[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]) == 13
assert Solution().countPyramids([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 0
assert Solution().countPyramids([[1, 1, 1], [1, 1, 1]]) == 2
assert Solution().countPyramids([[0, 1, 1, 0], [1, 1, 1, 1]]) == 2

#
# @lcpr case=start
# [[0,1,1,0],[1,1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[0,0,0],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]\n
# @lcpr case=end

#
