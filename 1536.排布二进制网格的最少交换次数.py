#
# @lc app=leetcode.cn id=1536 lang=python3
#
# [1536] 排布二进制网格的最少交换次数
#
from sbw import *
# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N=len(grid)
        counter=[0]*N
        for r,row in enumerate(grid):
            zeros=0
            for j in range(N-1,-1,-1):
                if row[j]==0:
                    zeros+=1
                else:
                    break
            counter[r]=zeros
        
        ret=0

        for r in range(N):
            need=N-1-r
            t=0
            for i,c in enumerate(counter):
                if c==-1:
                    continue
                if c>=need:
                    ret+=t
                    counter[i]=-1
                    break
                t+=1
            else:
                return -1
        return ret
# @lc code=end
assert Solution().minSwaps([[1,0,0],[1,1,0],[1,1,1]])==0
assert Solution().minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])==-1
assert Solution().minSwaps([[0,0,1],[1,1,0],[1,0,0]])==3
