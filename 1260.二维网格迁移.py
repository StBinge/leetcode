#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#
from sbw import *
# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R,C=len(grid),len(grid[0])
        ret=[[0]*C for _ in range(R)]
        tot=R*C
        for r in range(R):
            for c in range(C):
                idx=(r*C+c+k)%tot
                dr,dc=idx//C,idx%C
                ret[dr][dc]=grid[r][c]
        return ret
# @lc code=end
assert Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)==[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
assert Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)==[[9,1,2],[3,4,5],[6,7,8]]
