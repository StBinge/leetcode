#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#
from typing import List
# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        dp=[0]*n
        size=[0]*n
        def dfs(cur,parent):
            size[cur]=1
            dp[cur]=0
            for child in graph[cur]:
                if child==parent:
                    continue
                dfs(child,cur)
                dp[cur]+=dp[child]+size[child]
                size[cur]+=size[child]
        
        dfs(0,-1)
        ret=[0]*n
        def dfs2(cur,parent):
            ret[cur]=dp[cur]
            for child in graph[cur]:
                if child==parent:
                    continue
                cur_dp=dp[cur]
                cur_size=size[cur]
                child_dp=dp[child]
                child_size=size[child]

                dp[cur]-=dp[child]+size[child]
                size[cur]-=size[child]
                dp[child]+=dp[cur]+size[cur]
                size[child]+=size[cur]
                dfs2(child,cur)
                dp[cur]=cur_dp
                dp[child]=child_dp
                size[cur]=cur_size
                size[child]=child_size
        
        dfs2(0,-1)
        return ret

# @lc code=end
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
ret=[8,12,6,10,10,10]
assert Solution().sumOfDistancesInTree(n,edges)==ret