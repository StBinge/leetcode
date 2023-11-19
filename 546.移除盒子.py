#
# @lc app=leetcode.cn id=546 lang=python3
#
# [546] 移除盒子
#
from typing import List
# @lc code=start
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        L=len(boxes)
        dp=[[[0]*L for _ in range(L)] for _ in range(L)]
        for l in range(L-1,-1,-1):
            for r in range(l,L):
                for k in range(L-r):
                    if r>l and boxes[r]==boxes[r-1]:
                        dp[l][r][k]=dp[l][r-1][k+1]
                        continue
                    dp[l][r][k]=dp[l][r-1][0]+(k+1)**2
                    for i in range(l,r):
                        if boxes[i]==boxes[r]:
                            dp[l][r][k]=max(dp[l][r][k],dp[l][i][k+1]+dp[i+1][r-1][0])
        return dp[0][-1][0]



        # def get_points(l,r,k):
        #     if l>r:
        #         return 0
        #     if dp[l][r][k]!=0:
        #         return dp[l][r][k]
        #     r1=r
        #     k1=k
        #     while r1>l and boxes[r1-1]==boxes[r1]:
        #         r1-=1
        #         k1+=1
        #     ret=get_points(l,r1-1,0)+(k1+1)**2
        #     for i in range(l,r1):
        #         if boxes[i]==boxes[r1]:
        #             ret=max(ret,get_points(l,i,k1+1)+get_points(i+1,r1-1,0))
        #     dp[l][r][k]=ret
        #     return ret
        # return get_points(0,L-1,0)
# @lc code=end

assert Solution().removeBoxes([2,5,10,9,4,8,6,9,9,1])==16
assert Solution().removeBoxes([1,3,2,2,2,3,4,3,1])==23
assert Solution().removeBoxes([1,1,1])==9