#
# @lc app=leetcode.cn id=3128 lang=python3
# @lcpr version=30204
#
# [3128] 直角三角形
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        cols=[sum(col)-1 for col in zip(*grid)]

        ret=0
        for r in range(R):
            rows=sum(grid[r])-1
            for c in range(C):
                if grid[r][c]==0:
                    continue
                ret+=rows*cols[c]
        return ret
# @lc code=end
assert Solution().numberOfRightTriangles()


#
# @lcpr case=start
# [[0,1,0],[0,1,1],[0,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,1,0,1],[1,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[1,0,0],[1,0,0]]\n
# @lcpr case=end

#

