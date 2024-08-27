#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
#
from sbw import *


# @lc code=start
class Union:
    def __init__(self, n) -> None:
        self.sz = [1] * n
        self.p = list(range(n))

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def connect(self, x, y):
        x, y = self.find(x), self.find(y)
        self.p[x]=y
        # if x == y:
        #     return
        # if self.sz[x] > self.sz[y]:
        #     self.p[y] = x
        #     self.sz[x] += self.sz[y]
        # else:
        #     self.p[x] = y
        #     self.sz[y] += self.sz[x]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        initial_set = [0] * n
        for v in initial:
            initial_set[v] = 1

        union=Union(n)

        for u in range(n):
            if initial_set[u]==1:
                continue
            for v in range(u+1,n):
                if initial_set[v]==1:
                    continue
                if graph[u][v]==1:
                    union.connect(u,v)

        infected_by=[[] for _ in range(n)]
        for v in initial:
            infected=[0]*n

            for u in range(n):
                if initial_set[u]==1 or graph[u][v]==0:
                    continue
                infected[union.find(u)]=1
            
            for u in range(n):
                if infected[u]==1:
                    infected_by[u].append(v)

        cnt = [0] * n
        for u in range(n):
            if len(infected_by[u]) !=1:
                continue
            v=infected_by[u][0]
            for w in range(n):
                if union.find(w)==union.find(u):
                    cnt[v]+=1

        ret=initial[0]
        ma=cnt[ret]
        for i in initial:
            if cnt[i] > ma or (cnt[i]==ma and i<ret):
                ret = i
                ma = cnt[i]
        return ret


# @lc code=end
assert (
    Solution().minMalwareSpread([[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,1],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,1,0,0,0,0,0,1]],[2,1,9])
    == 9
)
assert (
    Solution().minMalwareSpread([[1,1,0,0],[1,1,0,1],[0,0,1,0],[0,1,0,1]],[3,0])
    == 0
)
assert (
    Solution().minMalwareSpread([[1,0,0,0,0,1,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[1,0,0,0,0,1,0],[0,0,0,0,0,0,1]],[4])
    == 4
)
assert (
    Solution().minMalwareSpread(graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1])
    == 1
)
assert (
    Solution().minMalwareSpread(graph=[[1, 1, 0], [1, 1, 1], [0, 1, 1]], initial=[0, 1])
    == 1
)
assert (
    Solution().minMalwareSpread(graph=[[1, 1, 0], [1, 1, 0], [0, 0, 1]], initial=[0, 1])
    == 0
)
