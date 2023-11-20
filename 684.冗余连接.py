#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#
from typing import List
# @lc code=start
class Union:
    def __init__(self,n) -> None:
        self.n=n
        self.p=[i for i in range(n)]

    def find(self,x):
        _x=x
        while x!=self.p[x]:
            x=self.p[x]
        self.p[_x]=x
        return x

    def connect(self,x,y):
        self.p[self.find(x)]=self.find(y)
    
    def is_connected(self,x,y):
        return self.find(x)==self.find(y)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union=Union(len(edges)+1)
        for x,y in edges:
            if union.is_connected(x,y):
                return [x,y]
            union.connect(x,y)
# @lc code=end
edges = [[1,2], [1,3], [2,3]]
assert Solution().findRedundantConnection(edges)==[2,3]
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
assert Solution().findRedundantConnection(edges)==[1,4]
