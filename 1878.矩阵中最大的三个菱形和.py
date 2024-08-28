#
# @lc app=leetcode.cn id=1878 lang=python3
#
# [1878] 矩阵中最大的三个菱形和
#
from sbw import *
# @lc code=start
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ret=[-1]*3
        R,C=len(grid),len(grid[0])

        def update(val):
            if val>ret[0]:
                ret[0],ret[1],ret[2]=val,ret[0],ret[1]
                return
            if val==ret[0]:
                return
            if val>ret[1]:
                ret[1],ret[2]=val,ret[1]
                return
            if val==ret[1]:
                return
            if val>ret[2]:
                ret[2]=val

        sumLT=[[0]*(C+2) for _ in range(R+1)]
        sumRT=[[0]*(C+2) for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                sumRT[r+1][c+1]=grid[r][c]+sumRT[r][c+2]
                sumLT[r+1][c+1]=grid[r][c]+sumLT[r][c]

        def count(r,c,l):
            if l==0:
                return grid[r][c]
            top_r,top_c=r-l,c
            bottom_r,bottom_c=r+l,c
            left_r,left_c=r,c-l
            right_r,right_c=r,c+l
            ret=sumRT[left_r+1][left_c+1]-sumRT[top_r][top_c+2]
            ret+=sumRT[bottom_r+1][bottom_c+1]-sumRT[right_r][right_c+2]
            ret+=sumLT[right_r][right_c]-sumLT[top_r+1][top_c+1]
            ret+=sumLT[bottom_r][bottom_c]-sumLT[left_r+1][left_c+1]
            return ret
            


        for r in range(R):
            for c in range(C):
                max_len=min(c,C-1-c,R-1-r,r)
                for l in range(max_len+1):
                    val=count(r,c,l)
                    update(val)
        return [v for v in ret if v>0]

# @lc code=end
assert Solution().getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]])==[228,216,211]
assert Solution().getBiggestThree([[1,2,3],[4,5,6],[7,8,9]])==[20,9,8]
assert Solution().getBiggestThree( [[7,7,7]])==[7]
