#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#
from sbw import *
# @lc code=start
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:


        initial.sort()
        N=len(graph)
        p=list(range(N))
        sz=[1]*N
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        
        def connect(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            p[py]=px
            sz[px]+=sz[py]
        
        def size(x):
            return sz[find(x)]
        
        for i in range(N):
            for j in range(i+1,N):
                if graph[i][j]:
                    connect(i,j)
                    # print(i,j)

        cnt={}
        for n in initial:
            pn=find(n)
            cnt[pn]=cnt.get(pn,0)+1

        max_con=0
        ret=-1
        for n in initial:
            if cnt[find(n)]>1:
                continue
            s=size(n)
            if s>max_con:
                ret=n
                max_con=s
        return ret if ret >=0 else initial[0]

# @lc code=end
graph=[[1,0,0,0,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,1,0],[0,0,0,0,0,0,1,1,0,0,0],[0,0,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,1]]
initial=[7,8,6,2,3]
assert Solution().minMalwareSpread(graph,initial)==2

graph=[[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]]
initial=[0,1,3]
assert Solution().minMalwareSpread(graph,initial)==3

graph=[[1,1,0],[1,1,0],[0,0,1]]
initial=[0,1,2]
assert Solution().minMalwareSpread(graph,initial)==2

graph = [[1,1,1],[1,1,1],[1,1,1]]
initial = [1,2]
assert Solution().minMalwareSpread(graph,initial)==1

graph = [[1,0,0],[0,1,0],[0,0,1]]
initial = [0,2]
assert Solution().minMalwareSpread(graph,initial)==0

graph = [[1,1,0],[1,1,0],[0,0,1]]
initial = [0,1]
assert Solution().minMalwareSpread(graph,initial)==0
