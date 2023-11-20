#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
from typing import List
# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        ancester=[i for i in range(len(edges)+1)]
        def find(x):
            if x!=ancester[x]:
                ancester[x]=find(ancester[x])
            return ancester[x]
        
        # set x as y's parent
        def connect(x,y):
            ancester[find(y)]=find(x)
        parents=ancester.copy()
        conflict,cycle=-1,-1
        for i,[x,y] in enumerate(edges):
            if parents[y]!=y:
                conflict=i
            else:
                parents[y]=x
            
                if find(x)==find(y):
                    cycle=i
                else:
                    connect(x,y)
        
        if conflict<0:
            return edges[cycle]
        if cycle>0:
            
            return [parents[edges[conflict][1]],edges[conflict][1]]
        else:
            return edges[conflict]

# @lc code=end
edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
ret= Solution().findRedundantDirectedConnection(edges)
assert ret ==[4,1]
edges=[[3,1],[4,2],[1,4],[2,1]]
assert Solution().findRedundantDirectedConnection(edges)==[2,1]

edges = [[1,2], [1,3], [2,3]]
assert Solution().findRedundantDirectedConnection(edges)==[2,3]