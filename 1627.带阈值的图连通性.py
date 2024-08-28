#
# @lc app=leetcode.cn id=1627 lang=python3
#
# [1627] 带阈值的图连通性
#
from sbw import *
# @lc code=start
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold==0:
            return [True]*len(queries)

        p=list(range(n+1))
        size=[1]*(n+1)
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        
        def is_connected(x,y):
            return find(x)==find(y)

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            
            if size[px]<size[py]:
                px,py=py,px
            p[py]=px
            size[px]+=size[py]

        is_prime=[True]*(n+1)
        for i in range(threshold+1,n):
            if not is_prime[i]:
                continue
            for j in range(2*i,n+1,i):
                union(i,j)
                is_prime[j]=False
        ret=[]
        for x,y in queries:
            ret.append(is_connected(x,y))
        return ret
# @lc code=end
assert Solution().areConnected(n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]])==eval_list_str('[false,false,false,false,false]')
assert Solution().areConnected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]])==eval_list_str('[true,true,true,true,true]')
assert Solution().areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]])==eval_list_str('[false,false,true]')
