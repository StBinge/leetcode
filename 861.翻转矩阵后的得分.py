#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#
from typing import List
# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        # row_flip=[False]*R
        # col_flip=[False]*C

        ret=0
        ret+=(1<<(C-1))*R
        for c in range(1,C):
            one_cnt=0
            for r in range(R):               
                if (grid[r][c]==1 and grid[r][0]==1) or (grid[r][c]==0 and grid[r][0]==0) :
                    one_cnt+=1
            ret+=(1<<(C-1-c))*max(one_cnt,R-one_cnt)
        return ret
# @lc code=end

grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
assert Solution().matrixScore(grid)==39
assert Solution().matrixScore([[0]])==1