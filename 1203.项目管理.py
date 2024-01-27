#
# @lc app=leetcode.cn id=1203 lang=python3
#
# [1203] 项目管理
#
from sbw import *
# @lc code=start
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i]<0:
                group[i]=m
                m+=1
        g_adj=[[] for _ in range(m)]
        item_adj=[[] for _ in range(n)]
        g_indegree=[0]*m
        item_indegree=[0]*n
        for i in range(n):
            g=group[i]
            for prev in beforeItems[i]:
                item_adj[prev].append(i)
                item_indegree[i]+=1
                pg=group[prev]
                if pg==g:
                    continue
                g_adj[pg].append(g)
                g_indegree[g]+=1
        
        def topological_sort(adj:list,indegree:list,n:int):
            ret=[]
            q=deque()
            for i in range(n):
                if indegree[i]==0:
                    q.append(i)
            while q:
                x=q.popleft()
                ret.append(x)
                for nxt in adj[x]:
                    indegree[nxt]-=1
                    if indegree[nxt]==0:
                        q.append(nxt)
            return ret if len(ret)==n else []

        sorted_g=topological_sort(g_adj,g_indegree,m)
        if not sorted_g:
            return []
        
        sorted_item=topological_sort(item_adj,item_indegree,n)
        if not sorted_item:
            return []

        g_items=[[] for _ in range(m)]
        for item in sorted_item:
            g_items[group[item]].append(item)
        
        ret=[]
        for g in sorted_g:
            ret.extend(g_items[g])
        return ret
# @lc code=end
print(Solution().sortItems(10,4,[0,1,1,2,3,-1,0,0,0,1],[[2,5],[3,5,4,6,8,7,2],[7],[],[],[],[],[],[],[]]))
print(Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]))
print(Solution().sortItems(5,5,[2,0,-1,3,0],[[2,1,3],[2,4],[],[],[]]))
print(Solution().sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))
