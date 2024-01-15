#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
from sbw import *
# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        left=[[0]*(C+1) for _ in range(R+1)]
        up=[[0]*(C+1) for _ in range(R+1)]
        ret=0
        for i in range(1,R+1):
            for j in range(1,C+1):
                if grid[i-1][j-1]==0:
                    continue
                left[i][j]=left[i][j-1]+1
                up[i][j]=up[i-1][j]+1
                border=min(left[i][j],up[i][j])
                while left[i-border+1][j]<border or up[i][j-border+1]<border:
                    border-=1
                ret=max(ret,border)
        return ret*ret




# @lc code=end
assert Solution().largest1BorderedSquare(grid = [[1,1,0,0]])==1
assert Solution().largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]])==9
