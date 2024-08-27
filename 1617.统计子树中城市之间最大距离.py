#
# @lc app=leetcode.cn id=1617 lang=python3
#
# [1617] 统计子树中城市之间最大距离
#
from sbw import *
# @lc code=start
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        dist=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v in edges:
            u-=1
            v-=1
            graph[u].append(v)
            graph[v].append(u)
            dist[u][v]=dist[v][u]=1

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if dist[j][i]!=float('inf') and dist[i][k]!=float('inf'):
                        dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])

        def dfs(u,pre,x,y,d):
            if dist[u][x]>d or dist[u][y]>d:
                return 1
            if (dist[u][x]==d and u<y) or (dist[u][y]==d and u<x):
                return 1
            ret=1
            for nxt in graph[u]:
                if nxt==pre:
                    continue
                ret*=dfs(nxt,u,x,y,d)

            if dist[u][x]+dist[u][y]>d:
                ret+=1
            return ret

        ret=[0]*(n-1)

    
        for i in range(n):
            for j in range(i+1,n):
                ret[dist[i][j]-1]+=dfs(i,-1,i,j,dist[i][j])
        return ret
# @lc code=end
assert Solution().countSubgraphsForEachDiameter(5,[[1,2],[1,5],[2,4],[3,5]])==[4,3,2,1]
assert Solution().countSubgraphsForEachDiameter(n = 3, edges = [[1,2],[2,3]])==[2,1]
assert Solution().countSubgraphsForEachDiameter(n = 2, edges = [[1,2]])==[1]
assert Solution().countSubgraphsForEachDiameter(n = 4, edges = [[1,2],[2,3],[2,4]])==[3,4,0]
