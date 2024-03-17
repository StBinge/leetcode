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
        s=sum(balls)
        # half=s//2
        # tot=math.factorial(s)
        # for ball in balls:
        #     tot//=math.factorial(ball)
        tot=math.comb(s,s//2)
        k=len(balls)
        # idx_color=[-1]*s
        # pre=0
        # for i,ball in enumerate(balls):
        #     for _ in range(ball):
        #         idx_color[pre]=i
        #         pre+=1
        left=[0]*k
        left[-1]=balls[-1]
        for i in range(k-2,-1,-1):
            left[i]=left[i+1]+balls[i]

        @cache
        def dp(idx,extra_cnt,extra_color):
            if idx==k:
                return int(extra_cnt==extra_color==0)
            remain=left[idx]
            if abs(extra_cnt)>remain:
                return 0
            ret=0
            b=balls[idx]
            for i in range(b+1):
                c=0
                if i==0:
                    c=-1
                elif i==b:
                    c=1
                ret+=math.comb(b,i)*dp(idx+1,extra_cnt-b+2*i,extra_color+c)
            return ret

        cnt=dp(0,0,0)
        return cnt/tot
# @lc code=end
assert abs(Solution().getProbability([1,2,1,2])-0.6)<1e-5
assert abs(Solution().getProbability([2,1,1])-0.66667)<1e-5
assert abs(Solution().getProbability(balls = [1,1])-1)<1e-5
