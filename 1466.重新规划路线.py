#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#
from sbw import *
# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges=[[] for _ in range(n)]
        for a,b in connections:
            edges[a].append([b,1])
            edges[b].append([a,0])

        ret=0
        q=[[0,-1]]
        # vis=[False]*n
        # vis[0]=True
        while q:
            cur,parent=q.pop()
            for nxt,cost in edges[cur]:
                if nxt==parent:
                    continue
                ret+=cost
                q.append([nxt,cur])
        return ret
    
# @lc code=end
assert Solution().minReorder(n = 3, connections = [[1,0],[2,0]])==0
assert Solution().minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]])==2
assert Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])==3
