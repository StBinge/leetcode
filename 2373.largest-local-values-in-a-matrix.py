#
# @lc app=leetcode.cn id=2373 lang=python3
# @lcpr version=30204
#
# [2373] 矩阵中的局部最大值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N=len(grid)
        ret=[[0]*(N-2) for _ in range(N-2)]
        for r in range(N):
            for c in range(N-2):
                # mx=0
                # for rr in range(r,r+3):
                #     mx=max(mx,max(grid[rr][c:c+3]))
                # ret[r][c]=mx
                grid[r][c]=max(grid[r][c:c+3])
        for r in range(N-2):
            for c in range(N-2):
                ret[r][c]=max(grid[x][c] for x in range(r,r+3))
        return ret
        
# @lc code=end



#
# @lcpr case=start
# [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]\n
# @lcpr case=end

#

