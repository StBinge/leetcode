#
# @lc app=leetcode.cn id=1042 lang=python3
#
# [1042] 不邻接植花
#
from sbw import *
# @lc code=start
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        edges=[[] for _ in range(n)]                                   
        for x,y in paths:
            x-=1
            y-=1
            edges[x].append(y)
            edges[y].append(x)

        ret=[0]*n
        for i in range(n):
            used=0
            for j in edges[i]:
                used |= 1<< ret[j]
            for k in range(1,5):
                if used & (1<<k)==0:
                    ret[i]=k
                    break
        return ret
# @lc code=end
n = 3
paths = [[1,2],[2,3],[3,1]]
assert Solution().gardenNoAdj(n,paths)==[1,2,3]
