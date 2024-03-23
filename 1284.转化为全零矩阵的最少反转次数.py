#
# @lc app=leetcode.cn id=1284 lang=python3
#
# [1284] 转化为全零矩阵的最少反转次数
#
from sbw import *
# @lc code=start
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        R,C=len(mat),len(mat[0])
        def flip(mat,r,c):
            mat[r][c]^=1
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=dirs[i]+r,dirs[i+1]+c
                if 0<=nr<R and 0<=nc<C:
                    mat[nr][nc]^=1
        ret=10**9
        for i in range(1<<C):
            cnt=0
            _mat=[row.copy() for row in mat]
            for j in range(C):
                if i & 1<<j:
                    flip(_mat,0,j)
                    cnt+=1
            for r in range(1,R):
                for c in range(C):
                    if _mat[r-1][c]==1:
                        flip(_mat,r,c)
                        cnt+=1
            if all(c==0 for c in _mat[-1]):
                ret=min(ret,cnt)
        return ret if ret<10**9 else -1
            
# @lc code=end
assert Solution().minFlips([[1,1,1],[1,0,1],[0,0,0]])==6
assert Solution().minFlips([[1,0,0],[1,0,0]])==-1
assert Solution().minFlips([[0]])==0
assert Solution().minFlips([[0,0],[0,1]])==3
