#
# @lc app=leetcode.cn id=1761 lang=python3
#
# [1761] 一个图中连通三元组的最小度数
#
from sbw import *
# @lc code=start
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(set)
        h=defaultdict(list)
        degree=[0]*(n+1)
        for x,y in edges:
            degree[x]+=1
            degree[y]+=1
            graph[x].add(y)
            graph[y].add(x)

        for x,y in edges:
            if degree[x]>degree[y] or (x>y and degree[x]==degree[y]):
                h[x].append(y)
            else:
                h[y].append(x)
        
        ret=float('inf')
        for i in range(1,n+1):
            for j in h[i]:
                for k in h[j]:
                    if k in graph[i]:
                        ret=min(ret,degree[i]+degree[j]+degree[k]-6)
        return ret if ret<len(edges) else -1
# @lc code=end
assert Solution().minTrioDegree(6,[[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]])==3
assert Solution().minTrioDegree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]])==0
assert Solution().minTrioDegree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]])==3
