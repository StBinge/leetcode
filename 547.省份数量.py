#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
from typing import List
# @lc code=start
class Union:
    def __init__(self,unions:list[list]) -> None:
        L=len(unions)
        self.count=L

        self.parents=[i for i in range(L)]
        self.weights=[1]*L
        for i in range(L):
            for j in range(i+1,L):
                if unions[i][j]:
                    self.connect(i,j)
    
    def find(self,x):
        if x!=self.parents[x]:
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    
    def connect(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x==root_y:
            return
        self.count-=1
        if self.weights[root_x]>=self.weights[root_y]:
            self.parents[root_y]=root_x
        else:
            self.parents[root_x]=root_y
        if self.weights[root_x]==self.weights[root_y]:
            self.weights[root_x]+=1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ret= Union(isConnected).count
        return ret
# @lc code=end

assert Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])==2
assert Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])==2
assert Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])==3
