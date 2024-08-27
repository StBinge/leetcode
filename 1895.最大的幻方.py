#
# @lc app=leetcode.cn id=1895 lang=python3
#
# [1895] 最大的幻方
#
from sbw import *
# @lc code=start
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        presums=[[0]*(C+1) for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                presums[r+1][c+1]=presums[r+1][c]+presums[r][c+1]-presums[r][c]+grid[r][c]
        
        def block_sum(r1,c1,r2,c2):
            return presums[r2+1][c2+1]-presums[r2+1][c1]-presums[r1][c2+1]+presums[r1][c1]

        def check(r,c,k):
            rr,cc=r+k-1,c+k-1
            avg=block_sum(r,c,rr,cc)//k
            dia1=dia2=0
            r1,c1=r,c
            r2,c2=r,cc
            for i in range(k):
                if block_sum(r+i,c,r+i,cc)!=avg:
                    return False
                if block_sum(r,c+i,rr,c+i)!=avg:
                    return False
                dia1+=grid[r1][c1]
                dia2+=grid[r2][c2]
                r1+=1
                c1+=1
                r2+=1
                c2-=1
            return dia1==dia2==avg


        for i in range(min(R,C),1,-1):
            for r in range(R-i+1):
                for c in range(C-i+1):
                    if check(r,c,i):
                        return i
        return 1

# @lc code=end
assert Solution().largestMagicSquare([[5,1,3,1],[9,3,3,1],[1,3,3,8]])==2
assert Solution().largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]])==3
