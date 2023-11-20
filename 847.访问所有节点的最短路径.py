#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        dist=[[n+1]*n for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                dist[i][j]=dist[j][i]=1
                # dist[i][j]=1
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        
        f=[[float('inf')]*(1<<n) for _ in range(n)]
        for mask in range(1,1<<n):
            if (mask & (mask-1))==0:
                u=bin(mask).count('0')-1
                f[u][mask]=0
                continue
            for u in range(n):
                if mask & (1<<u)==0:
                    continue
                for v in range(n):
                    if v==u or (mask & (1<<v)==0):
                        continue
                    f[u][mask]=min(f[u][mask],dist[v][u]+f[v][mask^(1<<u)])
        return min(f[u][(1<<n)-1] for u in range(n))
# @lc code=end
graph = [[1,2,3],[0],[0],[0]]
assert Solution().shortestPathLength(graph)==4
assert Solution().shortestPathLength([[6,7],[6],[6],[5,6],[6],[3],[2,0,3,4,1],[0]])==10
