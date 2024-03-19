#
# @lc app=leetcode.cn id=1292 lang=python3
#
# [1292] 元素和小于等于阈值的正方形的最大边长
#
from sbw import *
# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        R=len(mat)
        C=len(mat[0])
        pre_sum=[[0]*(C+1) for _ in range(R+1)]
        for i in range(R):
            for j in range(C):
                pre_sum[i+1][j+1]=mat[i][j]+pre_sum[i][j+1]+pre_sum[i+1][j]-pre_sum[i][j]
        ret=0
        
        for i in range(R):
            for j in range(C):
                for k in range(ret,min(R-i,C-j)):
                    ii,jj=i+k,j+k
                    if pre_sum[ii+1][jj+1]-pre_sum[ii+1][j]-pre_sum[i][jj+1]+pre_sum[i][j]<=threshold:
                        ret=k+1
                    else:
                        break
        return ret
# @lc code=end

assert Solution().maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]],40184)==2
assert Solution().maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1)==0
assert Solution().maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4)==2