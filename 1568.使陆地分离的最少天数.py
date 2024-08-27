#
# @lc app=leetcode.cn id=1568 lang=python3
#
# [1568] 使陆地分离的最少天数
#
from sbw import *
# @lc code=start
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        # 使用并查集解答
        p=list(range(R*C))
        nodes=R*C
        ones=0
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            p[px]=py
            nonlocal nodes
            nodes-=1

        graph=[[] for _ in range(R*C)]
        for r in range(R):
            for c in range(C):
                idx=r*C+c
                if grid[r][c]==0:
                    nodes-=1
                    p[idx]=-1
                else:
                    ones+=1
                    if r>0 and grid[r-1][c]==1:
                        idx2=(r-1)*C+c
                        union(idx,idx2)
                        graph[idx].append(idx2)
                        graph[idx2].append(idx) 
                    if c>0 and grid[r][c-1]==1:
                        idx2=r*C+c-1
                        union(idx,idx2)
                        graph[idx].append(idx2)
                        graph[idx2].append(idx)
        # 如果联通分量大于1, 不用删除
        if nodes>1:
            return 0
        # 如果陆地数量=0, 不用删
        # 如果陆地数量=1, 删除1
        # 如果陆地数量=2, 删除2
        if ones<3:
            return ones
        
        # 使用Tarjan找割点
        # 只要找到一个割点, 即可返回
        time=0
        def tarjan(cur,par,root):
            nonlocal time
            time+=1
            dfn[cur]=low[cur]=time
            child=0
            for nxt in graph[cur]:
                if nxt==par:
                    continue
                if dfn[nxt]:
                    low[cur]=min(low[cur],dfn[nxt])
                else:
                    if cur==root:
                        child+=1
                    if child>1:
                        return True
                    if tarjan(nxt,cur,root):
                        return True
                    low[cur]=min(low[cur],low[nxt])
                    if cur!=root and low[nxt]>=dfn[cur]:
                        return True
            return False

        dfn=[0]*(R*C)
        low=[0]*(R*C)
        for i in range(R*C):
            if p[i]==-1:
                continue
            if dfn[i]==0 and tarjan(i,i,i):
                return 1

        # 两种方法都失败, 只能删除2
        return 2

# @lc code=end
assert Solution().minDays([[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]])==1
assert Solution().minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]])==2
assert Solution().minDays([[1,1]])==2
