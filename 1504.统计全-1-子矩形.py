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
        for r in range(R):
            stack=[]
            s=0
            for c in range(C):

                if mat[r][c]==0:
                    cols[c]=0
                    stack=[]
                    s=0
                    continue
                else:
                    cols[c]+=1
                h=cols[c]
                w=1
                while stack and stack[-1][0]>=h:
                    pre_h,pre_w=stack.pop()
                    s-=(pre_h-h)*pre_w
                    w+=pre_w
                s+=h
                ret+=s
                stack.append([h,w])
        return ret

# @lc code=end
assert Solution().numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])==24
assert Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]])==13
