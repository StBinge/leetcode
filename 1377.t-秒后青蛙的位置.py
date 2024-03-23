#
# @lc app=leetcode.cn id=1377 lang=python3
#
# [1377] T 秒后青蛙的位置
#
from sbw import *
# @lc code=start
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph=[[] for _ in range(n+1)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        graph[1].append(0)

        def dfs(cur,prev,t):
            if t==0 or len(graph[cur])==1:
                return int(target==cur)
            if cur==target:
                return len(graph[cur])==1
            for nxt in graph[cur]:
                if nxt==prev:
                    continue
                prod=dfs(nxt,cur,t-1)
                if prod:
                    return prod*(len(graph[cur])-1)
            return 0
        
        prod=dfs(1,0,t)
        if prod:
            return 1/prod
        return 0
        
# @lc code=end
assert abs(Solution().frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],20,6)-0.16667)<=10**-5 
assert abs(Solution().frogPosition(8,[[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]],7,7)-0)<=10**-5 
assert abs(Solution().frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4)-0.16666666666666666)<=10**-5 
