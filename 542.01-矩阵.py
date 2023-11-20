#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R,C=len(mat),len(mat[0])
        dis=[[float('inf')]*C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if mat[r][c]==0:
                    dis[r][c]=0
        
        for r in range(R):
            for c in range(C):
                if r>0:
                    dis[r][c]=min(dis[r][c],dis[r-1][c]+1)
                if c>0:
                    dis[r][c]=min(dis[r][c],dis[r][c-1]+1)
        
        for r in range(R-1,-1,-1):
            for c in range(C-1,-1,-1):
                if r+1<R:
                    dis[r][c]=min(dis[r][c],dis[r+1][c]+1)
                if c+1<C:
                    dis[r][c]=min(dis[r][c],dis[r][c+1]+1)
        return dis
# @lc code=end
assert Solution().updateMatrix([[0],[1]]) == [[0],[1]]
assert Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
assert Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
