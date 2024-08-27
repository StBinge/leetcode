#
# @lc app=leetcode.cn id=1786 lang=python3
#
# [1786] 从第一个节点出发到最后一个节点的受限路径数
#
from sbw import *
# @lc code=start
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        Mod=10**9+7
        adj=defaultdict(list)
        for x,y,w in edges:
            adj[x].append([y,w])
            adj[y].append([x,w])
        
        dist=[float('inf')]*(n+1)
        dist[n]=0
        vis=[False]*(n+1)
        queue=[[0,n]]
        while queue:
            d,idx=heapq.heappop(queue)
            if vis[idx]:
                continue
            vis[idx]=True
            for nxt,w in adj[idx]:
                dist[nxt]=min(dist[nxt],d+w)
                heapq.heappush(queue,[d+w,nxt])
        
        sorted_idx=sorted(range(1,n+1),key=dist.__getitem__)

        f=[0]*(n+1)
        f[n]=1
        for i in range(n):
            idx=sorted_idx[i]
            d=dist[idx]
            for nxt,_ in adj[idx]:
                if d>dist[nxt]:
                    f[idx]+=f[nxt]
                    f[idx]%=Mod
            if idx==1:
                break
        return f[1]

# @lc code=end
assert Solution().countRestrictedPaths(n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]])==1
assert Solution().countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]])==3
