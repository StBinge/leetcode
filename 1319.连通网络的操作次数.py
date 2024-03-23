#
# @lc app=leetcode.cn id=1319 lang=python3
#
# [1319] 连通网络的操作次数
#
from sbw import *
# @lc code=start
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        p=list(range(n))
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        def connect(x,y):
            x,y=find(x),find(y)
            if x==y:
                return
            p[x]=y
        for x,y in connections:
            connect(x,y)
        
        parts=sum(i==p[i] for i in range(n))
        return parts-1
        
# @lc code=end
assert Solution().makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]])==0
assert Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]])==-1
assert Solution().makeConnected(4,connections = [[0,1],[0,2],[1,2]])==1
