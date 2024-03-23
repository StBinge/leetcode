#
# @lc app=leetcode.cn id=3067 lang=python3
#
# [3067] 在带权树网络中统计可连接服务器对数目
#
from sbw import *
# @lc code=start
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        N=len(edges)+1
        graph=[[] for _ in range(N)]
        for x,y,w in edges:
            graph[x].append([y,w])
            graph[y].append([x,w])
        
        def dfs(parent,cur,dis):
            ret=int(dis%signalSpeed==0)
            for x,xw in graph[cur]:
                if x==parent:
                    continue
                ret+=dfs(cur,x,dis+xw)
            return ret


        ret=[0]*N
        for i,links in enumerate(graph):
            s=0
            for j,jw in links:
                cnt=dfs(i,j,jw)
                ret[i]+=cnt*s
                s+=cnt
        return ret
# @lc code=end

assert Solution().countPairsOfConnectableServers(edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3)==[2,0,0,0,0,0,2]
assert Solution().countPairsOfConnectableServers(edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1)==[0,4,6,6,4,0]