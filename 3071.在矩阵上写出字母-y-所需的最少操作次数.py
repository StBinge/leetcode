#
# @lc app=leetcode.cn id=3071 lang=python3
#
# [3071] 在矩阵上写出字母 Y 所需的最少操作次数
#
from sbw import *
# @lc code=start
class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        counter=[0]*3
        N=len(grid)
        for r in range(N):
            for c in range(N):
                counter[grid[r][c]]+=1
        y_counter=[0]*3
        center=N//2
        for r in range(center):
            val=grid[r][r]
            counter[val]-=1
            y_counter[val]+=1
            val=grid[r][N-1-r]
            counter[val]-=1
            y_counter[val]+=1
        for r in range(center,N):
            val=grid[r][center]
            counter[val]-=1
            y_counter[val]+=1
        
        max_keep=0
        for i in range(3):
            for j in range(3):
                if i!=j:
                    max_keep=max(max_keep,y_counter[i]+counter[j])
        return N*N-max_keep

# @lc code=end
assert Solution().minimumOperationsToWriteY([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]])==12
assert Solution().minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]])==3
