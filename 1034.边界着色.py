#
# @lc app=leetcode.cn id=1034 lang=python3
#
# [1034] 边界着色
#
from sbw import *


# @lc code=start
class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]]:
        if color == grid[row][col]:
            return grid
        rows, cols = len(grid), len(grid[0])
        q = [[row, col]]
        tc = grid[row][col]
        vis = set()
        while q:
            r, c = q.pop()
            vis.add((r, c))
            dirs = [-1, 0, 1, 0, -1]
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i + 1]
                if nr<0 or nr==rows or nc<0 or nc==cols :
                    grid[r][c]=color
                elif (nr,nc) in vis:
                    continue
                elif grid[nr][nc]!=tc:
                    grid[r][c] = color
                else:
                    q.append([nr,nc])
        return grid


# @lc code=end
grid=[[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]]
row=1
col=3
color=1
assert Solution().colorBorder(grid,row,col,color) == [[1,1,1,1,1,2],[1,2,1,1,1,2],[1,1,1,1,1,2]]

args = exec_expression("grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2")
assert Solution().colorBorder(**args) == [[2,2,2],[2,1,2],[2,2,2]]

args = exec_expression("grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3")
assert Solution().colorBorder(**args) == [[1, 3, 3], [2, 3, 3]]

args = exec_expression("grid = [[1,1],[1,2]], row = 0, col = 0, color = 3")
assert Solution().colorBorder(**args) == [[3, 3], [3, 2]]
