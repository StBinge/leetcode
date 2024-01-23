#
# @lc app=leetcode.cn id=1223 lang=python3
#
# [1223] 掷骰子模拟
#
from sbw import *
# @lc code=start
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        Mod=10**9+7

        f=[[0]*6 for _ in range(n)]
        f[0]=[1]*6
        s=[0]*n
        s[0]=6
        for i in range(1,n):
            for j in range(6):
                res=s[i-1]
                idx=i-rollMax[j]-1
                if i==rollMax[j]:
                    res-=1
                elif i>rollMax[j]:
                    res-=s[idx]-f[idx][j]
                f[i][j]=res%Mod
            s[i]=sum(f[i])%Mod
        return s[-1]
# @lc code=end
assert Solution().dieSimulator(n = 20, rollMax = [8,5,10,8,7,2])==822005673
assert Solution().dieSimulator(n = 3, rollMax = [1,1,1,2,2,3])==181
assert Solution().dieSimulator(n = 2, rollMax = [1,1,2,2,2,3])==34
