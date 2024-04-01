#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#
from sbw import *
# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        pos=[0]*n
        pos[start_node]=1
        graph=[[] for _ in range(n)]
        for [x,y],p in zip(edges,succProb):
            graph[x].append([y,p])
            graph[y].append([x,p])
        
        h=[(-1,start_node)]
        while h:
            prop,cur=heapq.heappop(h)
            prop=-prop
            if pos[cur]>prop:
                continue
            for nxt,nxt_p in graph[cur]:
                _p=prop*nxt_p
                if pos[nxt]<_p:
                    heapq.heappush(h,(-_p,nxt))
                    pos[nxt]=_p
        return pos[end_node]
# @lc code=end
def test(n,edges,succProb,start,end,result):
    ans=Solution().maxProbability(n,edges,succProb,start,end)
    assert abs(ans-result)<1e-5

test(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2,result=0.25)
