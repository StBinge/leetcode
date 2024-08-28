#
# @lc app=leetcode.cn id=1808 lang=python3
#
# [1808] 好因子的最大数目
#
from sbw import *
# @lc code=start
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors<=4:
            return primeFactors
        m=primeFactors%3
        Mod=10**9+7

        if m==0:
            return pow(3,primeFactors//3,Mod)%Mod
        
        if m==1:
            return 4*pow(3,primeFactors//3-1,Mod)%Mod


        return 2*pow(3,primeFactors//3,Mod)%Mod
# @lc code=end

