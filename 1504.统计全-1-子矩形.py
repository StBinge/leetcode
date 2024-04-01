#
# @lc app=leetcode.cn id=1504 lang=python3
#
# [1504] 统计全 1 子矩形
#
from sbw import *
# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R,C=len(mat),len(mat[0])
        cols=[0]*C
        ret=0
        for i in range(R):
            stack=[]
            s=0
            for j in range(C):

                if mat[i][j]==1:
                    cols[j]=cols[j]+1
                else:
                    cols[j]=0
                w=1
                while stack and stack[-1][0]>cols[j]:
                    s-=stack[-1][1]*(stack[-1][0]-cols[j])
                    w+=stack[-1][1]
                    stack.pop()
                s+=cols[j]
                ret+=s
                stack.append([cols[j],w])
        return ret
# @lc code=end
assert Solution().numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])==24
assert Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]])==13
