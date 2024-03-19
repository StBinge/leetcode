#
# @lc app=leetcode.cn id=1467 lang=python3
#
# [1467] 两个盒子中球的颜色数相同的概率
#
from sbw import *
# @lc code=start
import math
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        N=sum(balls)
        L=len(balls)
        left=[0]*len(balls)
        left[-1]=balls[-1]
        for i in range(len(balls)-2,-1,-1):
            left[i]=left[i+1]+balls[i]
        
        def dfs(idx,dif_color,dif_cnt):
            if idx==L:
                return dif_color==dif_cnt==0
            if abs(dif_cnt)>left[idx]:
                return 0
            ret=0
            n=balls[idx]
            ret=dfs(idx+1,dif_color-1,dif_cnt-n)
            ret+=dfs(idx+1,dif_color+1,dif_cnt+n)
            for k in range(1,n):
                ret+=math.comb(n,k) * dfs(idx+1,dif_color,dif_cnt-n+2*k)
            return ret
        return dfs(0,0,0) / math.comb(N,N//2)
# @lc code=end

assert abs(Solution().getProbability([6])-1)<=1e-5
assert abs(Solution().getProbability([2,1,1])-0.66667)<=1e-5
assert abs(Solution().getProbability([1,1])-1.0)<=1e-5