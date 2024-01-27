#
# @lc app=leetcode.cn id=1192 lang=python3
#
# [1192] 查找集群内的关键连接
#
from sbw import *
# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjcent=[[] for _ in range(n)]
        for a,b in connections:
            adjcent[a].append(b)
            adjcent[b].append(a)
        
        visit_time=[-1]*n
        ret=[]
        # time=-1
        def dfs(cur,prev,time):
            # nonlocal time
            if visit_time[cur]<0:
                
                visit_time[cur]=time
                for nxt in adjcent[cur]:
                    if nxt==prev:
                        continue
                    nxt_time=dfs(nxt,cur,time+1)
                    visit_time[cur]=min(visit_time[cur],nxt_time)
                    if nxt_time > time:
                        ret.append([cur,nxt])

            return visit_time[cur]
        
        dfs(0,-1,0)
        return ret
# @lc code=end
assert sorted(Solution().criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))==sorted([[1,3]])
assert sorted(Solution().criticalConnections(n = 2, connections = [[0,1]]))==sorted([[0,1]])
