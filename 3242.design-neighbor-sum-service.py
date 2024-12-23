#
# @lc app=leetcode.cn id=3242 lang=python3
# @lcpr version=30204
#
# [3242] 设计相邻元素求和服务
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid=grid
        self.R=len(grid)
        self.C=len(grid[0])
        self.pos={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.pos[grid[i][j]]=[i,j]
        

    def adjacentSum(self, value: int) -> int:
        r,c=self.pos[value]
        ret=0
        dirs=[-1,0,1,0,-1]
        for i in range(4):
            nr,nc=r+dirs[i],c+dirs[i+1]
            if 0<=nr<self.R and 0<=nc<self.C:
                ret+=self.grid[nr][nc]
        return ret

    def diagonalSum(self, value: int) -> int:
        r,c=self.pos[value]
        ret=0
        for dr,dc in [[1,1],[-1,1],[-1,-1],[1,-1]]:
            nr,nc=r+dr,c+dc
            if 0<=nr<self.R and 0<=nc<self.C:
                ret+=self.grid[nr][nc]
        return ret


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
# @lc code=end


ops=["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]
args=[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
obj=NeighborSum(args[0][0])

ret= eval_list_str('[null, 6, 16, 16, 4]')

test_obj(obj,ops,args,ret)


#
# @lcpr case=start
# ["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"][[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]\n
# @lcpr case=end

# @lcpr case=start
# ["neighborSum", "adjacentSum", "diagonalSum"][[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]\n
# @lcpr case=end

#

