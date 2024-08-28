#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#
from sbw import *
# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        C=len(mat[0])
        for r,row in enumerate(mat):
            cnt=sum(row)-(r==0)
            if cnt>0:
                for c,v in enumerate(row):
                    if v==1:
                        mat[0][c]+=cnt
        return sum(mat[0][j]==1 for j in range(C))
# @lc code=end
assert Solution().numSpecial([[1,0,0],[0,1,0],[0,0,1]])==3
