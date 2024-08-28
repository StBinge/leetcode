#
# @lc app=leetcode.cn id=1595 lang=python3
#
# [1595] 连通两组点的最小成本
#
from sbw import *


# @lc code=start
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        s1, s2 = len(cost), len(cost[0])
        Mask=1<<s2
        # f=[[float('inf')]*Mask for _ in range(s1+1)]
        # f[0][0]=0
        f0=[float('inf')]*Mask
        f1=[0]*Mask
        f0[0]=0
        for i in range(s1):
            for mask in range(Mask):
                f1[mask]=float('inf')
                for j in range(s2):
                    if mask & (1<<j) ==0:
                        continue
                    f1[mask]=min(f1[mask],f0[mask^(1<<j)]+cost[i][j])
                    f1[mask]=min(f1[mask],f0[mask]+cost[i][j])
                    f1[mask]=min(f1[mask],f1[mask^(1<<j)]+cost[i][j])
            f0,f1=f1,f0
        return f0[-1]


# @lc code=end
assert Solution().connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10
assert Solution().connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4
assert Solution().connectTwoGroups([[15, 96], [36, 2]]) == 17
