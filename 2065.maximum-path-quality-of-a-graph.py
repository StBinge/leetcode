#
# @lc app=leetcode.cn id=2065 lang=python3
# @lcpr version=30204
#
# [2065] 最大化一张图中的路径价值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        N=len(values)
        adj=defaultdict(list)
        for x,y,t in edges:
            adj[x].append([y,t])
            adj[y].append([x,t])
        
        q=[[0,0]]
        dist=[float('inf')]*N
        dist[0]=0
        while q:
            cost,cur=heapq.heappop(q)
            if cost>dist[cur]:
                continue
            for nxt,time in adj[cur]:
                _cost=cost+time
                if _cost<dist[nxt]:
                    dist[nxt]=_cost
                    heapq.heappush(q,[_cost,nxt])

        # adj=defaultdict(list)
        # dist[0]=0
        # for x,y,t in edges:
        #     if dist[x]*2>maxTime or dist[y]*2>maxTime:
        #         continue
        #     adj[x].append([y,t])
        #     adj[y].append([x,t])
        
        vis=[0]*N
        vis[0]=1
        ret=0
        def dfs(cost,cur,val):
            if cur==0:
                nonlocal ret
                ret=max(ret,val)
            for nxt,t in adj[cur]:
                if dist[nxt]+cost+t>maxTime:
                    continue
                _val=val+(vis[nxt]==0)*values[nxt]
                vis[nxt]+=1
                dfs(cost+t,nxt,_val)
                vis[nxt]-=1
        
        dfs(0,0,values[0])
        return ret
# @lc code=end
assert Solution().maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30)==25
assert Solution().maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49)==75


#
# @lcpr case=start
# [0,32,10,43]\n[[0,1,10],[1,2,15],[0,3,10]]\n49\n
# @lcpr case=end

# @lcpr case=start
# [5,10,15,20]\n[[0,1,10],[1,2,10],[0,3,10]]\n30\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n[[0,1,10],[1,2,11],[2,3,12],[1,3,13]]\n50\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n[[1,2,10]]\n10\n
# @lcpr case=end

#

