#
# @lc app=leetcode.cn id=1905 lang=python3
# @lcpr version=30204
#
# [1905] 统计子岛屿
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R,C=len(grid1),len(grid1[0])
        ret=0
        dirs=[-1,0,1,0,-1]
        for r in range(R):
            for c in range(C):
                if grid2[r][c]==1:
                    valid=True
                    q=[[r,c]]
                    while q:
                        x,y=q.pop()
                        grid2[x][y]=0
                        if grid1[x][y]==0:
                            valid=False
                        for i in range(4):
                            nx,ny=x+dirs[i],y+dirs[i+1]
                            if 0<=nx<R and 0<=ny<C and grid2[nx][ny]==1:
                                q.append([nx,ny])
                    ret+=valid
        return ret
# @lc code=end
assert Solution().countSubIslands([[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]],[[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]])==0
assert Solution().countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]])==2
assert Solution().countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])==3


#
# @lcpr case=start
# [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]\n[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]\n
# @lcpr case=end

#

