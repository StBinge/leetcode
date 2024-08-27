#
# @lc app=leetcode.cn id=1579 lang=python3
#
# [1579] 保证图可完全遍历
#
from sbw import *
# @lc code=start

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # graph=[[[] for _ in range(3)] for _ in range(n+1)]
        # for t,u,v in edges:
        #     graph[u][t].append(v)
        #     graph[v][t].append(u)
        
        p=list(range(n+1))
        size=[1]*(n+1)
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False
            if size[px]<size[py]:
                px,py=py,px
            p[py]=px
            size[px]+=size[py]
            return True

        ret=0
        for t,x,y in edges:
            if t!=3:
                continue
            if not union(x,y):
                ret+=1
        def simplify(type):
            nonlocal p,size
            _p=p.copy()
            _size=size.copy()
            ret=0
            for t,x,y in edges:
                if t!=type:
                    continue
                if not union(x,y):
                    ret+=1
            if all(size[i]<n for i in range(1,n+1)):
                ret=-1
            p,size=_p,_size
            return ret
        s1=simplify(1)
        if s1<0:
            return -1
        s2=simplify(2)
        if s2<0:
            return -1
        return ret+s1+s2

# @lc code=end

assert Solution().maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]])==-1
assert Solution().maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]])==0
assert Solution().maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])==2