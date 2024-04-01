#
# @lc app=leetcode.cn id=1489 lang=python3
#
# [1489] 找到最小生成树里的关键边和伪关键边
#
from sbw import *
# @lc code=start
class Union:
    def __init__(self,n) -> None:
        self.parent=list(range(n))
        self.size=[1]*n
        self.cnt=n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])

        return self.parent[x]

    def connect(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return False
        if self.size[y]>self.size[x]:
            x,y=y,x
        self.parent[y]=x
        self.size[x]+=self.size[y]
        self.cnt-=1
        return True

class Tarjan:
    def __init__(self,n:int,edges:list[list],eids:list[list]) -> None:
        self.n=n
        self.edges=edges
        self.eids=eids
        self.dfn=[-1]*n
        self.low=[-1]*n
        self.ts=0
        self.ans=[]
    
    def _get_cutting_edge(self,x:int,p_eid:int):
        self.dfn[x]=self.low[x]=self.ts
        self.ts+=1
        for nxt,eid in zip(self.edges[x],self.eids[x]):
 
            if self.dfn[nxt]==-1:
                self._get_cutting_edge(nxt,eid)
                self.low[x]=min(self.low[x],self.low[nxt])
                if self.low[nxt]>self.dfn[x]:
                    self.ans.append(eid)
            elif eid!=p_eid:
                self.low[x]=min(self.low[x],self.low[nxt])
        
    

    def get_cutting_edge(self):
        for i in range(self.n):
            if self.dfn[i]==-1:
                self._get_cutting_edge(i,-1)
        return self.ans

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m=len(edges)

        
        for i,edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x:x[2])

        ans0=[]
        ans1=[]
        label=[0]*m
        i=0
        un=Union(n)
        while i<m:
            w=edges[i][2]
            j=i+1
            while j<m and edges[j][2]==w:
                j+=1
            
            id_map={}
            gm=defaultdict(list)
            gmid=defaultdict(list)
            idx=0
            for k in range(i,j):
                x,y,w,eid=edges[k]
                x=un.find(x)
                y=un.find(y)
                if x==y:
                    label[eid]=-1
                    continue
                if x not in id_map:
                    id_map[x]=idx
                    idx+=1
                x=id_map[x]
                if y not in id_map:
                    id_map[y]=idx
                    idx+=1
                y=id_map[y]
                gm[x].append(y)
                gmid[x].append(eid)
                gm[y].append(x)
                gmid[y].append(eid)

            bridges=Tarjan(idx,gm,gmid).get_cutting_edge()
            ans0.extend(bridges)
            for x in bridges:
                label[x]=1
            
            for k in range(i,j):
                un.connect(edges[k][0],edges[k][1])
            i=j
            if un.cnt==1:
                break
        for x,y,w,eid in edges[:i]:
            if label[eid]==0:
                ans1.append(eid)
        return [ans0,ans1]
# @lc code=end
def test(answer,n,edges):
    ret=Solution().findCriticalAndPseudoCriticalEdges(n, edges)
    for r,a in zip(ret,answer):
        assert sorted(r)==sorted(a), f'{r}\t{a}'


test([[13,16,45,55,57,58,61,89],[10,15,23,25,28,32,37,39,51,54,70,75,76,85]],14,[[0,1,13],[0,2,6],[2,3,13],[3,4,4],[0,5,11],[4,6,14],[4,7,8],[2,8,6],[4,9,6],[7,10,4],[5,11,3],[6,12,7],[12,13,9],[7,13,2],[5,13,10],[0,6,4],[2,7,3],[0,7,8],[1,12,9],[10,12,11],[1,2,7],[1,3,10],[3,10,6],[6,10,4],[4,8,5],[1,13,4],[11,13,8],[2,12,10],[5,8,1],[3,7,6],[7,12,12],[1,7,9],[5,9,1],[2,13,10],[10,11,4],[3,5,10],[6,11,14],[5,12,3],[0,8,13],[8,9,1],[3,6,8],[0,3,4],[2,9,6],[0,11,4],[2,5,14],[4,11,2],[7,11,11],[1,11,6],[2,10,12],[0,13,4],[3,9,9],[4,12,3],[6,7,10],[6,8,13],[9,11,3],[1,6,2],[2,4,12],[0,10,3],[3,12,1],[3,8,12],[1,8,6],[8,13,2],[10,13,12],[9,13,11],[2,11,14],[5,10,9],[5,6,10],[2,6,9],[4,10,7],[3,13,10],[4,13,3],[3,11,9],[7,9,14],[6,9,5],[1,5,12],[4,5,3],[11,12,3],[0,4,8],[5,7,8],[9,12,13],[8,12,12],[1,10,6],[1,9,9],[7,8,9],[9,10,13],[8,11,3],[6,13,7],[0,12,10],[1,4,8],[8,10,2]])
test([[0,1],[2,3,4,5]],n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])
test([[3],[0,1,2,4,5,6]],6,[[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]])
test([[],[0,1,2,3]],n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])