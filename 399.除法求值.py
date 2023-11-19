#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from typing import List
# @lc code=start
class Union:
    def __init__(self,length:int) -> None:
        self.parents=[i for i in range(length)]
        self.weights=[1 for _ in range(length)]
    
    def find(self,x):

        if x!=self.parents[x]:
            origin=self.parents[x]
            self.parents[x]=self.find(self.parents[x])
            self.weights[x]*=self.weights[origin]
        return self.parents[x]

    def connect(self,x:int,y:int,value):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX==rootY:
            return
        self.parents[rootX]=rootY
        self.weights[rootX]=self.weights[y]*value/self.weights[x]

    def is_connected(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX==rootY:
            return self.weights[x]/self.weights[y]
        else:
            return -1



class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        union=Union(len(equations)*2)
        id_map={}
        id=0
        for i in range(len(values)):
            x,y=equations[i]
            if x not in id_map:
                id_map[x]=id
                id+=1
            if y not in id_map:
                id_map[y]=id
                id+=1
            union.connect(id_map[x],id_map[y],values[i])
        ret=[-1]*len(queries)
        for i,(x,y) in enumerate(queries):
            idx=id_map.get(x,-1)
            idy=id_map.get(y,-1)
            if idx<0 or idy<0:
                continue
            ret[i]=union.is_connected(idx,idy)
        return ret

# @lc code=end
equations =[["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
r=Solution().calcEquation(equations,values,queries)
print(r)


equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
r=Solution().calcEquation(equations,values,queries)
print(r)


equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
r=Solution().calcEquation(equations,values,queries)
print(r)


