#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#
from sbw import *
# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        props=[0]*n
        props[start_node]=1
        graph=[[] for _ in range(n)]
        for [x,y],p in zip(edges,succProb):
            graph[x].append((y,p))
            graph[y].append((x,p))
        min_heap=[[-1,start_node]]
        while min_heap:
            cur_p,cur_node=heapq.heappop(min_heap)
            cur_p=-cur_p
            if cur_p<props[cur_node]:
                continue
            for nxt_node,p in graph[cur_node]:
                nxt_p=cur_p*p
                if nxt_p>props[nxt_node]:
                    props[nxt_node]=nxt_p
                    heapq.heappush(min_heap,[-nxt_p,nxt_node])
        return props[end_node]
# @lc code=end
def test(n,edges,succProb,start,end,result):
    ans=Solution().maxProbability(n,edges,succProb,start,end)
    assert abs(ans-result)<1e-5

test(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2,result=0.25)
