#
# @lc app=leetcode.cn id=882 lang=python3
#
# [882] 细分图中的可到达节点
#
from typing import List
# @lc code=start
# from collections import deque
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:

        graph=[[] for _ in range(n)]
        # edge_vis={}
        for x,y,d in edges:
            graph[x].append([y,d])
            graph[y].append([x,d])
        
        q=[[0,0]]
        ret=0
        vis=set()
        # dis=[0]*n
        used={}
        while q:
            step,x =heapq.heappop(q)
            if x in vis:
                continue
            vis.add(x)
            ret+=1
            for y,nodes in graph[x]:
                if step+1+nodes<=maxMoves and y not in vis:
                    # ret+=1
                    heapq.heappush(q,[step+1+nodes,y])
                used[(x,y)]=max(0,maxMoves-step)
        for x,y,nodes in edges:
            ret+=min(nodes,used.get((x,y),0)+used.get((y,x),0))
        return ret


# @lc code=end
edges = [[0,1,10],[0,2,1],[1,2,2]]
maxMoves = 6
n = 3
assert Solution().reachableNodes(edges,maxMoves,n)==13