#
# @lc app=leetcode.cn id=1473 lang=python3
#
# [1473] 粉刷房子 III
#
from sbw import *
# @lc code=start
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        Max=float('inf')
        houses=[h-1 for h in houses]

        f=[[[Max]*target for _ in range(n)] for _ in range(m)]
        best=[[[-1,Max,Max] for _ in range(target)] for _ in range(m)]
        
        # best0=best[0][0]
        # if houses[0]==-1:
        #     for i in range(n):
        #         f[0][i][0]=cost[0][i]
        #         if cost[0][i]<best0[1]:
        #             best0[0],best0[1],best0[2]=i,cost[0][i],best0[1]
        #         elif cost[0][i]<best0[2]:
        #             best0[2]=cost[0][i]
        # else:
        #     f[0][houses[0]][0]=0
        #     best0[0],best0[1]=houses[0],0
        
        for i in range(m):
            for j in range(n):
                if houses[i]!=-1 and houses[i]!=j:
                    continue
                for k in range(min(i+1,target)):
                    v=Max
                    if i==0:
                        if k==0:
                            v=0
                    else:
                        v=f[i-1][j][k]
                        if k>0:
                            _best=best[i-1][k-1]
                            if j==_best[0]:
                                v=min(v,_best[2])
                            else:
                                v=min(v,_best[1])
                    if houses[i]==-1:
                        v+=cost[i][j]
                    f[i][j][k]=v
                    cur_best=best[i][k]
                    if v<cur_best[1]:
                        cur_best[0],cur_best[1],cur_best[2]=j,v,cur_best[1]
                    elif v<cur_best[2]:
                        cur_best[2]=v
        
        ret=min(f[-1][c][target-1] for c in range(n))
        return ret if ret<Max else -1

# @lc code=end
assert Solution().minCost([0,1,0,0,1,2,0,0,2,1],[[4,5,2,6],[8,3,2,9],[6,7,3,1],[10,10,2,7],[6,5,2,4],[4,4,3,9],[9,8,3,5],[7,9,10,3],[8,5,9,10],[10,7,4,6]],10,4,6)==24
assert Solution().minCost([2,2,1],[[1,1],[3,4],[4,2]],3,2,2)==0
assert Solution().minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3)==-1
assert Solution().minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5)==5
assert Solution().minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)==11
assert Solution().minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)==9
