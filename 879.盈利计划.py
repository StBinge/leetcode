#
# @lc app=leetcode.cn id=879 lang=python3
#
# [879] 盈利计划
#
from typing import List
# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        Mod=10**9+7
        l=len(group)
        # f=[[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(l+1)]
        f=[[0] * (minProfit+1) for _ in range(n+1)]
        for i in range(n+1):
            f[i][0]=1
        
        for pro,people in zip(profit,group):
            for j in range(n,-1,-1):
                for k in range(minProfit,-1,-1):
                    if j>=people:
                        f[j][k]+=f[j-people][max(0,k-pro)]
                    f[j][k]%=Mod
        return f[-1][-1]
# @lc code=end
n = 10
minProfit = 5
group = [2,3,5]
profit = [6,7,8]
assert Solution().profitableSchemes(n,minProfit,group,profit)==7
