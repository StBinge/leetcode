#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        rg=[[] for _ in range(n)]
        for i,nodes in enumerate(graph):
            for node in nodes:
                rg[node].append(i)
        in_deg=[len(nodes) for nodes in graph]
        queue=deque([i for i in range(n) if in_deg[i]==0])
        while queue:
            node=queue.popleft()
            for j in rg[node]:
                in_deg[j]-=1
                if in_deg[j]==0:
                    queue.append(j)
        return [i for i in range(n) if in_deg[i]==0]
# @lc code=end
graph=[[],[0,2,3,4],[3],[4],[]]
assert Solution().eventualSafeNodes(graph)==[0,1,2,3,4]

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
assert Solution().eventualSafeNodes(graph)==[2,4,5,6]
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
assert Solution().eventualSafeNodes(graph)==[4]
